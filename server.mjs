import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('.', import.meta.url));
const port = Number(process.env.PORT || 3000);
const mime = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.csv': 'text/csv; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.ico': 'image/x-icon'
};

async function send(res, path) {
  try {
    const info = await stat(path);
    if (!info.isFile()) throw new Error('not a file');
    const body = await readFile(path);
    res.writeHead(200, {
      'Content-Type': mime[extname(path)] || 'application/octet-stream',
      'Cache-Control': 'no-cache'
    });
    res.end(body);
  } catch {
    res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Not found');
  }
}

createServer(async (req, res) => {
  const raw = new URL(req.url || '/', 'http://localhost').pathname;
  const safe = normalize(raw).replace(/^\.\.(\/|\\|$)/, '');
  if (safe === '/manus-routes.json') return send(res, join(root, 'public/manus-routes.json'));
  if (safe.startsWith('/data/')) return send(res, join(root, 'public', safe));
  const candidate = safe === '/' ? join(root, 'index.html') : join(root, safe);
  try {
    const info = await stat(candidate);
    if (info.isFile()) return send(res, candidate);
  } catch {}
  return send(res, join(root, 'index.html'));
}).listen(port, '0.0.0.0', () => {
  console.log(`[quietalert] listening on 0.0.0.0:${port}`);
});
