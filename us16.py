from prettytable import PrettyTable

def sameLastName(inputs):
    for i in inputs():
        print()

#Function to write the table 
def table(lists):
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age',
                     'Alive', 'Death', 'Child', 'Spouse']

    for i in lists:
        x.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
    print("\nIndividuals")
    print(x)

def main(lists):
    table(sameLastName(lists))