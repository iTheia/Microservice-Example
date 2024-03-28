import { Module } from '@nestjs/common';
import { LoginModule } from './modules/login/login.module';
import { TokenModule } from './modules/token/token.module';
import { ConfigModule, ConfigService } from '@nestjs/config';
import config from './config';
import { MongooseModule } from '@nestjs/mongoose';

@Module({
  imports: [
    ConfigModule.forRoot({
      load: [config],
      isGlobal: true,
    }),
    MongooseModule.forRootAsync({
      inject: [ConfigService],
      useFactory: (config: ConfigService) => {
        return {
          uri: config.get('databaseUrl'),
          retryAttempts: 5,
          retryDelay: 1000,
        };
      },
    }),
    LoginModule,
    TokenModule,
  ],
})
export class AppModule {}
