import { readFileSync } from 'fs';
import { join } from 'path';

export default () => ({
  port: parseInt(process.env.PORT, 10),
  databaseUrl: process.env.DATABASE_URL,
  accessToken: {
    private: readFileSync(
      join(__dirname, '../', '../', 'static', 'access-token-private.pem'),
    ),
    public: readFileSync(
      join(__dirname, '../', '../', 'static', 'access-token-public.pem'),
    ),
  },
  refreshToken: {
    private: readFileSync(
      join(__dirname, '../', '../', 'static', 'refresh-token-private.pem'),
    ),
    public: readFileSync(
      join(__dirname, '../', '../', 'static', 'refresh-token-public.pem'),
    ),
  },
});
