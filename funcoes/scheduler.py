import schedule
import time

def agendar_tarefa(funcao, intervalo_minutos=None, horario_fixo=None):
    """
    Agenda a execução de uma função de duas formas:
    - A cada X minutos (intervalo_minutos)
    - Em um horário fixo do dia (horario_fixo, ex: "08:00")

    Obs: Somente uma das opções deve ser usada por vez.
    """

    if intervalo_minutos:
        # Executa a cada X minutos
        schedule.every(intervalo_minutos).minutes.do(funcao)
        print(f"⏳ Tarefa agendada para rodar a cada {intervalo_minutos} minuto(s).")

    elif horario_fixo:
        # Executa todo dia no horário informado
        schedule.every().day.at(horario_fixo).do(funcao)
        print(f"⏰ Tarefa agendada para rodar todo dia às {horario_fixo}.")

    else:
        print("⚠️ Você precisa informar intervalo_minutos ou horario_fixo.")
        return

    # Loop infinito para manter o agendamento rodando
    while True:
        schedule.run_pending()
        time.sleep(1)
