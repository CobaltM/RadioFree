## Usage

`deepKill` helps cleanup zombie child processes while for example doing some TDD that creates loads of them and failed to remove them for unobvious reasons.

```js
import deepKill from 'deepkill';
import {spawn} from 'child_process';

const p = spawn('long-process-with-forks.js');

// Do stuff...

deepKill(p.pid);

// Continue doing stuff...
```

## License !heading

deepkill is [MIT licensed](./LICENSE).

© 2017 [Jason Lenoble](mailto:jason.lenoble@gmail.com)
