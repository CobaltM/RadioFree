import {expect} from 'chai';
import {spawn} from 'child_process';
import path from 'path';
import {makeSingleTest} from 'child-process-data';
import deepKill from '../src/deepkill';

describe('Testing deepKill', function () {
  this.timeout(5000); // eslint-disable-line no-invalid-this

  it(`Cluncky test relying on Un*x env`, function () {
    const while1File = path.join(__dirname, 'scripts/while1.js');
    const p = spawn('node', [while1File]);

    return new Promise(resolve => {
      setTimeout(resolve, 1000);
    }).then(() => {
      const test = makeSingleTest({
        childProcess: ['ps', ['-u']],

        checkResults (res) {
          expect(res.out()).to.match(new RegExp(
            `\\s+${p.pid}\\s+.*node .*while1.js`));
          expect(res.out()).to.match(/.*node .*while2.js/);
          expect(res.out()).to.match(/.*node .*while3.js/);
        },

        tearDownTest () {
          deepKill(p.pid);
        },
      });

      return test();
    }).then(() => {
      return new Promise(resolve => {
        setTimeout(resolve, 1000);
      });
    }).then(() => {
      const test = makeSingleTest({
        childProcess: ['ps', ['-u']],

        checkResults (res) {
          expect(res.out()).not.to.match(new RegExp(
            `\\s+${p.pid}\\s+.*node .*while1.js`));
          expect(res.out()).not.to.match(/.*node .*while2.js/);
          expect(res.out()).not.to.match(/.*node .*while3.js/);
        },
      });

      return test();
    });
  });
});
