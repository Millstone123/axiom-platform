// Axiom Platform — Entry Point
// BUG: Missing database URL validation causes silent connection failure

import { createServer } from './server.js';     // ERR_MODULE_NOT_FOUND — triggers diagnostic
import { connectDatabase } from './db.js';
import { loadConfig } from './config.js';

const config = loadConfig();
await connectDatabase(config.DATABASE_URL);

const server = createServer(config);
server.listen(config.PORT, () => {
  console.log(`Axiom running on :${config.PORT}`);
});
