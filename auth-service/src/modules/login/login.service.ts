import { Injectable } from '@nestjs/common';
import {
  LoginDto,
  RenewAccessTokenDto,
  RegisterDto,
  ValidateTokenDto,
} from './dto';
import { InjectModel } from '@nestjs/mongoose';
import { Login } from './entities/login.entity';
import { Model } from 'mongoose';
import { TokenService } from '../token/token.service';

@Injectable()
export class LoginService {
  constructor(
    @InjectModel(Login.name) private repository: Model<Login>,
    private tokenService: TokenService,
  ) {}

  async register(registerDto: RegisterDto) {
    const login = new this.repository(registerDto);
    const account = await login.save();
    return this.tokenService.createTokenPair(account.toJSON());
  }

  async login(login: LoginDto) {
    const account = await this.repository.findOne({ email: login.email });
    return this.tokenService.createTokenPair(account.toJSON());
  }

  async validateToken(validateToken: ValidateTokenDto) {
    return this.tokenService.verifyToken(
      validateToken.token,
      validateToken.type,
    );
  }

  async renewAccessToken(renewAccessToken: RenewAccessTokenDto) {
    const validatedPayload = this.tokenService.verifyRefreshToken(
      renewAccessToken.refreshToken,
    );
    const account = await this.repository.findOne({
      email: validatedPayload?.email,
    });
    return {
      access: this.tokenService.createAccessToken(account.toJSON()),
    };
  }
}
