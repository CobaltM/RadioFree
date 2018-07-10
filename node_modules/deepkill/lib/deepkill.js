'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = deekKill;

var _psTree = require('ps-tree');

var _psTree2 = _interopRequireDefault(_psTree);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function deekKill(pid, _signal, _callback) {
  var signal = _signal || 'SIGKILL';
  var callback = _callback || function () {};

  (0, _psTree2.default)(pid, function (err, children) {
    [pid].concat(children.map(function (p) {
      return p.PID;
    })).forEach(function (tpid) {
      try {
        process.kill(tpid, signal);
      } catch (ex) {}
    });
    callback();
  });
}
module.exports = exports['default'];