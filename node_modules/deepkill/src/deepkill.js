import psTree from 'ps-tree';

export default function deekKill (pid, _signal, _callback) {
  const signal = _signal || 'SIGKILL';
  const callback = _callback || function () {};

  psTree(pid, function (err, children) {
    [pid].concat(
      children.map(function (p) {
        return p.PID;
      })
    ).forEach(function (tpid) {
      try {
        process.kill(tpid, signal);
      } catch (ex) {}
    });
    callback();
  });
}
