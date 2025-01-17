# Automatização para agendamento de refeições
#### Para almoçar e jantar no meu Campus Universitário, é necessário fazer agendamento de cada refeição, de forma individual e todos os dias (Também é possível agendar uma semana inteira de uma vez, mas leva um tempo considerável). O sistema de agendamento é ambíguo, demorado, e tedioso. Este algoritmo foi desenvolvido com o objetivo de realizar o agendamento de refeições do Restaurante Universitário de forma automatizada, para poupar tempo e garantir as refeições de forma simplificada.

# Como funciona o agendamento através desse sistema?
#### Este código:
- [x] Executa o navegador que o usuário desejar.¹
- [x] Abre a página de login.²
- [x] Se registra no sistema.³
- [x] Acessa o portal do estudante, bem como o menu de agendamento de refeições.
- [x] Realiza o agendamento de acordo com a quantidade de dias escolhida pelo usuário no início do programa.

######  1: Certos navegadores perguntam qual perfil o usuário gostaria de utilizar ao abrir o navegador. Para acessar o perfil desejado, o sistema pausa por cinco segundos para que você possa escolher. ATENÇÃO: o sistema não faz isso por você. Se o perfil não for escolhido nesse intervalo de cinco segundos, haverá problemas na automatização.
###### 2: Com o login e a senha que for inserida no início do programa.
###### 3: Você pode alterar o código-fonte e mudar as variáveis nav, login, e senha, caso não queira digitar manualmente todas estas opções sempre que rodar o programa. Basta procurar estas variáveis no início do código e substituir o texto após a igualdade ('=') com a entrada desejada.



# Observações
Para executar o programa, você pode:
  1. Abrir o terminal, digitar o caminho em que o arquivo está localizado, e executar.
  2. Abrir o arquivo através de um compilador, como o VsCode.
  3. Adicionar um atalho do arquivo à área de trabalho. Para que ele seja inicializado diretamente no Python, clique com o botão direito no atalho > Abri com > Python.
     
  O sistema utiliza como parâmetro a data atual do computador, e realiza agendamentos a partir do dia seguinte, já que o sistema de agendamentos não permite que se agende uma refeição no dia referente à mesma.

  O sistema foi pensado de forma que funcione de maneira universal em todos os computadores, mas foi projetado em uma única máquina, o que significa que não há parâmetros suficientes para concluir que funcionará perfeitamente em todas as máquinas. Um fator de bastante valia, por exemplo, é o tempo de processamento ou de abertura de uma aba/navegador, que pode variar bastante (afetando as instruções do algoritmo, que foram programadas para durar um tempo específico).

  O sistema foi feito para ignorar fins de semana, pois são dias em que o Restaurante Universitário não se encontra em funcionamento. Independetemente da quantidade de dias, o número escolhido não sera perdido caso encontre fins de semana no caminho (Por exemplo: se hoje é sexta-feira, e cinco dias foram solicitados, o sábado e o domingo seguintes não reduzirão o número de dias desejados, e o agendamento será feito até a próxima sexta-feira, que é o quinto dia útil mais próximo).

# Requisitos
Para agendar refeições de forma automatizada com este programa, é necessário que:
- [x] A linguagem Python esteja instalada na máquina.
- [x] O download da biblioteca pyautogui seja feito.¹

###### 1: Para instalar o pyatogui, basta abrir o terminal do seu computador e digitar: "!pip install pyautogui". O Python já deve estar instalado.
