import path from 'path';
import {fork} from 'child_process';

const whileFile = path.join(__dirname, 'while3.js');

fork(whileFile);
