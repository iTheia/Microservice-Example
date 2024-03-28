import { Controller, Post, Body } from '@nestjs/common';
import { LoginService } from './login.service';
import {
  LoginDto,
  RenewAccessTokenDto,
  RegisterDto,
  ValidateTokenDto,
} from './dto';

@Controller('auth')
export class LoginController {
  constructor(private readonly loginService: LoginService) {}

  @Post('register')
  async register(@Body() registerDto: RegisterDto) {
    return this.loginService.register(registerDto);
  }

  @Post('login')
  async login(@Body() loginDto: LoginDto) {
    return this.loginService.login(loginDto);
  }

  @Post('validate-token')
  async validateToken(@Body() validateTokenDto: ValidateTokenDto) {
    return this.loginService.validateToken(validateTokenDto);
  }

  @Post('renew-access-token')
  async renewAccessToken(@Body() refreshTokenDto: RenewAccessTokenDto) {
    return this.loginService.renewAccessToken(refreshTokenDto);
  }
}
