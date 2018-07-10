import path from 'path';
import {fork} from 'child_process';

const whileFile = path.join(__dirname, 'while2.js');

fork(whileFile);
