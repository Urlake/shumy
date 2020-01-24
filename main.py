pergs = {
    "0": ["oi", "ola", "oie"],
    "1": ["urlake", "urlake"],
    "2": ["oscar", "oscar"],
    "3": ["shumy", "shumy"],
    "4": ["esta", "está", "estou"],
    "5": ["ai", "ai"],
    "6": ["tudo"],
    "7": ["bem", "bom"],
    "8": ["ok"],
    "9": ["sim", "claro", "também", "tambem", "tbm"],
    "10": ["oque", "oq", "que", "qual", "quantos", "quando"],
    "11": ["quer", "quero"],
    "12": ["fazer"],
    "13": ["eu", "me", "mim"],
    "14": ["você", "voce", "vc", "tu", "sua", "tua", "teu", "seu"],
    "15": ["idade", "data de aniversário", "data de aniversario", "nasceu", "anos", "ano"],
    "17": ["bonito", "lindo", "cheiroso", "legal", "daora", "incrivel", "bonita", "linda", "cheirosa"],
    "18": ["nome"],
    "19": ["gosta", "gostar", "gostaria", "gosto"],
    "20": ["filme"]
}

resps = {
    "Oie ^^": ["0 ", "0 3 "],
    "Papai?!": ["1 ", "13 1 "],
    "No que posso Ajudar?": ["4 5 ", "3 4 5 ", "14 ", "14 4 5 "],
    "Eu sou Shumy!!": ["0 1 ", "1 0 ", "0 2 ", "2 0 ", "10 14 18 ", "14 18 ", "14 18 10 "],
    "Estou bem, e Você?": ["6 7 ", "3 6 7 ", "6 7 3 ", "6 7 14 ", "14 7 ", "7 4 ", "4 7 ", "14 4 7 "],
    "Que Bom :D": ["4 7 ", "7 4 ", "9 ", "4 7 9 ", "9 4 7 ", "9 7 4 ", "13 4 7 ", "13 7 4 "],
    "Conversar ,_,": ["10 11 12 ", "11 12 10 ", "10 14 11 12 ", "14 11 12 10 "],
    "Não Sei ;-;": ["10 14 15 ", "10 15 14 "],
    "Brigado :3": ["3 14 17 ", "17 ", "14 17 "],
    "Claro!!": ["13 17 ", "14 17 13 ", "14 19 13 "], 
    "Meu Filme Preferido é o \"Cão e a Raposa\"": ["14 19 10 20 ", "10 20 14 19 ", "10 20 "],
    "Eu Também!!": ["13 19 20 ", "19 20 "],
    ":D": ["8 "],
    "...": [""]
}

while True:
    user = input('\nVocê: ').lower()
    l = 0
    number = ""
    bol = 0
    bol2 = 0
    message = user.replace('?','')
    message = message.replace('!','')
    message = message.replace(',','')
    message = message.replace('.','')
    msg = message.split()
    while l < len(msg):        
        for t in pergs:
            try:
                if pergs[str(t)][pergs[str(t)].index(msg[l])]:
                    number += str(t) + " "
            except:
                continue
        l += 1
    for v in resps:
        if bol == 0:
            try:
                if resps[v][resps[v].index(number)]:
                    bol2 = v
                    bol = 1
            except:
                bol2 = 0
                
                continue
    if bol2 != 0:
        print('\nShumy: ' + bol2)