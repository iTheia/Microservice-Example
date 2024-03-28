import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import * as jwt from 'jsonwebtoken';

interface Account {
  _id: string;
  email: string;
  role: string;
}
@Injectable()
export class TokenService {
  private access: any;
  private refresh: any;
  private accessConfig = {
    algorithm: 'RS256',
    expiresIn: '2 minutes',
    allowInsecureKeySizes: true,
  };
  private refreshConfig = {
    algorithm: 'RS256',
    expiresIn: '2 hours',
    allowInsecureKeySizes: true,
  };

  constructor(private config: ConfigService) {
    this.access = this.config.get('accessToken');
    this.refresh = this.config.get('refreshToken');
  }

  createRefreshToken(account: Account) {
    const token = jwt.sign(
      {
        email: account.email,
        id: account._id,
      },
      this.refresh.private,
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-expect-error
      this.refreshConfig,
    );
    return token;
  }

  createAccessToken(account: Account) {
    const token = jwt.sign(
      {
        email: account.email,
        role: account.role,
        id: account._id,
      },
      this.access.private,
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-expect-error
      this.accessConfig,
    );
    return token;
  }

  createTokenPair(account: Account) {
    return {
      access: this.createAccessToken(account),
      refresh: this.createRefreshToken(account),
    };
  }

  verifyRefreshToken(token: string): Account {
    return jwt.verify(token, this.refresh.public, {
      algorithms: ['RS256'],
      ignoreExpiration: false,
    }) as Account;
  }

  verifyAccessToken(token: string): Account {
    return jwt.verify(token, this.access.public, {
      algorithms: ['RS256'],
      ignoreExpiration: false,
    }) as Account;
  }

  verifyToken(token: string, type: 'access' | 'refresh') {
    if (!token) return false;
    if (!type) return false;
    if (type == 'refresh') {
      this.verifyRefreshToken(token);
    }
    if (type == 'refresh') {
      this.verifyAccessToken(token);
    }
    return true;
  }
}
