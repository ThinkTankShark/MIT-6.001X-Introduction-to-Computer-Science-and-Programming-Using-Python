def sumDigits(N):
  if N == 0:
    return 0
  else:
    return (N%10) + sumDigits(N//10)
