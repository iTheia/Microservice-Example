export class ValidateTokenDto {
  token: string;
  type: 'refresh' | 'access';
}
