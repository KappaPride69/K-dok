#!/usr/bin/env python3
def get_id(s):
    return int(s.split(":")[0])
    
    
def main():
    data = [ 
    (1, 'Albany', 'NY', 162692),
    (3, 'Allegany', 'NY', 11986),
    (121, 'Wyoming', 'NY', 8722),
    (123, 'Yates', 'NY', 5094)
]
    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(sorted(users,key=get_id,reverse=True))
    
    li=[ [2, 6], [1, 3], [5, 4] ]
    
    
    
if __name__ == "__main__":
    main()