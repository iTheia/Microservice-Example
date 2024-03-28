import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { HydratedDocument } from 'mongoose';

export type LoginDocument = HydratedDocument<Login>;

@Schema()
export class Login {
  @Prop({ unique: true, required: true })
  email: string;

  @Prop({ required: true })
  password: string;

  @Prop({ default: 'regular' })
  role: string;
}

export const LoginSchema = SchemaFactory.createForClass(Login);
