import { Module } from '@nestjs/common';
import { LoginService } from './login.service';
import { LoginController } from './login.controller';
import { MongooseModule } from '@nestjs/mongoose';
import { Login, LoginSchema } from './entities/login.entity';
import { TokenModule } from '../token/token.module';

@Module({
  imports: [
    MongooseModule.forFeature([{ name: Login.name, schema: LoginSchema }]),
    TokenModule,
  ],
  controllers: [LoginController],
  providers: [LoginService],
})
export class LoginModule {}
