


from requests import get,post
import platform
import re
import os

def Search_Menu():

  while 1:
    print("""  #####                                     
 #     # ######   ##   #####   ####  #    # 
 #       #       #  #  #    # #    # #    # 
  #####  #####  #    # #    # #      ###### 
       # #      ###### #####  #      #    # 
 #     # #      #    # #   #  #    # #    # 
  #####  ###### #    # #    #  ####  #    # 
                                            """)
    try:
      print("[0] Voltar")
      query = input("\nBuscar por: ")
      if query == "0":
        return
      else:
        html = get(url=f"https://tuaserie.space/pesquisa.php?q={query.replace(' ','%20')}").text
        infos = re.findall(r"<a href='([\w\/?\-?\_?\.?]+)'>([\w\ ?\.?\??\+?\/?\!?\:?\;?\-?\_?\|?\*?]+)</a>",html)
        if len(infos) == 0:
          print(f"\n'{query}' Nao Encontrado\n")
          continue
        Watch_Menu(infos)
    except Exception as e:
      print(e)

def Watch_Menu(infos):
  while 1:
    print(""" #     #                            
 #  #  #   ##   #####  ####  #    # 
 #  #  #  #  #    #   #    # #    # 
 #  #  # #    #   #   #      ###### 
 #  #  # ######   #   #      #    # 
 #  #  # #    #   #   #    # #    # 
  ## ##  #    #   #    ####  #    # 
                                    """)
    try:
      print("\n"*1)
      print("[0] Voltar")
      for n in range(0,len(infos)):
        print(f"[{n+1}]"+str(infos[n][1]))
      print("\n"*1)
      op = int(input("Escolha para assistir: ")) -1
      if op == -1:
        return
      else:
        url = "https://tuaserie.space"+infos[op][0]
        print(url)
        Season_Menu(url)
    except Exception as e:
      print(e)

def Season_Menu(url):
  while 1:
    try:
      html = get(url=url).text
      infos = re.findall(r'([\w]+): <a target="_blank" href="([\w\/?\.?\=?]+)" rel="nofollow">([\ ?\w]+)</a>',html)
      uniq_infos = []
      for n in range(0,len(infos)):
        #print(infos[n])
        try:
          if infos[n][0] == infos[n+1][0]:
            if not infos[n][1] in str(uniq_infos):
              if "DUBLADO" in str(infos[n][2]):
                dub = infos[n][1]; #print(dub,"gak")
              else:
                leg = infos[n][1]
              if "LEGENDADO" in str(infos[n+1][2]):
                leg = infos[n+1][1]; #print(leg,"ga")
              else:
                dub = infos[n+1][1]
              uniq_infos += [[infos[n][0],dub,leg]]
          else:
            if not infos[n][1] in str(uniq_infos):
              uniq_infos += [[infos[n][0],infos[n][1]]]
        except:
          None
      temp_num = 0
      print("\n[0] Voltar")
      #print(uniq_infos); exit()
      for n in range(0,len(uniq_infos)):
        if uniq_infos[n][0] == "01":
         temp_num += 1
         print(f"[{temp_num}] Temporada",temp_num)

      option = int(input("\nEscolha uma temporada: "))
      if option == 0:
        return
      else:
        Episode_Menu(option,uniq_infos)

    except Exception as e:
      print(e)

def Episode_Menu(season,uniq_infos):
  try:
    cont_temp = 0
    print("[0] Voltar")
    for n in range(0,len(uniq_infos)):
      if uniq_infos[n][0] == "01":
        cont_temp += 1
      if cont_temp == season:
        dbr = open(".tuaserie.txt").read()
        if uniq_infos[n][1].split("/").pop() in dbr:
          ini = "\033[94m"
        else:
          ini = "\033[0m"
        end = "\033[0m"
        print(f"{ini}[{int(uniq_infos[n][0])}] Episodio",uniq_infos[n][0],end)
    option = int(input("\nEscolha um Episodio: "))
    if option == 0:
      return
    if len(uniq_infos[option]) > 2:
      print("[0] Voltar")
      print("[1] Dublado")
      print("[2] Legendado")
      option2 = int(input("\nEscolha uma opcao: "))
      if option2 == 0:
        return
      else:
        cont_temp = 0
        for n in range(0,len(uniq_infos)):
          if uniq_infos[n][0] == "01":
            cont_temp += 1
          if cont_temp == season:
            if int(uniq_infos[n][0]) == option:
              url = "https://tuaserie.casa/include/player2.php?servers=" + uniq_infos[n][option2].split("/").pop()
              print(url)
              if platform.system() == "Linux":
                os.system(f"xdg-open {url}")
              elif platform.system() == "Windows":
                os.system(f"start {url}")
              dbw = open(".tuaserie.txt","a")
              dbw.write(url+"\n")
              dbw.close()
    else:
      cont_temp = 0
      for n in range(0,len(uniq_infos)):
        if uniq_infos[n][0] == "01":
          cont_temp += 1
        if cont_temp == season:
          if int(uniq_infos[n][0]) == option:
            url = "https://tuaserie.casa/include/player2.php?servers=" + uniq_infos[n][1].split("/").pop()
            print(url)
            os.system(f"xdg-open {url}")
            dbw = open(".tuaserie.txt","a")
            dbw.write(url+"\n")
            dbw.close()
  except Exception as e:
    print(e)


def Main_Menu():
  while 1:
    print(""" #######                #####                         
    #    #    #   ##   #     # ###### #####  # ###### 
    #    #    #  #  #  #       #      #    # # #      
    #    #    # #    #  #####  #####  #    # # #####  
    #    #    # ######       # #      #####  # #      
    #    #    # #    # #     # #      #   #  # #      
    #     ####  #    #  #####  ###### #    # # ###### 
                                                      """)
    print("[1] Proucurar por Series")
    #print("[2] Favoritos (not added)")
    print("[0] Sair")

    op = int(input("\nEscolha uma opcao: "))

    if op == 0:
      exit()
    elif op == 1:
      Search_Menu()
    elif op == 2:
      #Menu_Favoritos()
      None

Main_Menu()
