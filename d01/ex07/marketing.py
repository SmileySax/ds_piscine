import sys


def data() -> tuple:
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
               'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return clients, participants, recipients


def make_set(data: list) -> set:
    return set(data)


def manage_call_center(clients: set, recipients: set) -> set:
    return clients - recipients


def manage_potential_clients(clients: set, participants: set) -> set:
    return participants - clients


def manage_loyalty_program(clients: set, participants: set) -> set:
    return clients - participants


def manage_request(order: str):
    clients, participants, recipients = data()
    clients_set = make_set(clients)
    participants_set = make_set(participants)
    recipients_set = make_set(recipients)
    if order == 'call_center':
        res = manage_call_center(clients_set, recipients_set)
    elif order == 'potential_clients':
        res = manage_potential_clients(clients_set, participants_set)
    elif order == 'loyalty_program':
        res = manage_loyalty_program(clients_set, participants_set)
    else:
        raise ValueError('Please enter one of valid commands: call_center, potential_clients or loyalty_program')
    print(*res, sep='; ')


def main():
    if len(sys.argv) == 2:
        try:
            manage_request(sys.argv[1])
        except ValueError:
            print('Please enter one of valid commands: call_center, potential_clients or loyalty_program')


if __name__ == '__main__':
    main()
