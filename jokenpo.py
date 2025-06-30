import random

user_points = 0
computer_points = 0

options = ['r', 't', 'p']

while True:
    user_choice = (input('Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair. ')).lower()

    if user_choice == 'q':
        break

    if user_choice not in options:
        print('Digite novamente!')
        continue

    computer_choice = random.randint(0,2)
    # 0 : R, 1 : T, 2 : P
    computer_option = options[computer_choice]

    print('O computador escolheu ' + computer_option)

    if user_choice == computer_option:
        print('Empate!')

    elif user_choice == 'r' and computer_option == 't':
        print('Você ganhou!')
        user_points = user_points + 1

    elif user_choice == 't' and computer_option == 'p':
        print('Você ganhou!')
        user_points = user_points + 1

    elif user_choice == 'p' and computer_option == 'r':
        print('Você ganhou!')
        user_points = user_points + 1

    else:
        print('Você perdeu!')
        computer_points = computer_points + 1

print('A sua pontuação foi de ' + str(user_points) + ' pontos!')
print('A pontuação do computador foi de ' + str(computer_points) + ' pontos!')

if computer_points < user_points:
     print('A vitória é sua!')

elif computer_points > user_points:
    print('Você foi derrotado!')

else:
    print('Empate')

print('Até a próxima!')








