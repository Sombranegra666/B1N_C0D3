print("""
 $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\        $$$$$$$\    $$\   $$\   $$\ 
$$  __$$\ $$$ __$$\ $$  __$$\ $$ ___$$\       $$  __$$\ $$$$ |  $$$\  $$ |
$$ /  \__|$$$$\ $$ |$$ |  $$ |\_/   $$ |      $$ |  $$ |\_$$ |  $$$$\ $$ |
$$ |      $$\$$\$$ |$$ |  $$ |  $$$$$ /       $$$$$$$\ |  $$ |  $$ $$\$$ |
$$ |      $$ \$$$$ |$$ |  $$ |  \___$$\       $$  __$$\   $$ |  $$ \$$$$ |
$$ |  $$\ $$ |\$$$ |$$ |  $$ |$$\   $$ |      $$ |  $$ |  $$ |  $$ |\$$$ |
\$$$$$$  |\$$$$$$  /$$$$$$$  |\$$$$$$  |      $$$$$$$  |$$$$$$\ $$ | \$$ |
 \______/  \______/ \_______/  \______/       \_______/ \______|\__|  \__|
[By Dreifus] [v3.0]
 """)

print("[1]: Converter Numero Normal em Binário"), print("[2]: Converter bite Em Byte"),print("[3]: Converter Byte Em bite"), print()
pc1=int(input("> "))
if(pc1==1):
    print("[!!] Obs: Ignore o 0b [!!]")
    print("[|] set One Number"), print()
    n1=int(input("> "))
    n2=bin(n1)
    print("bin> {}".format(n2))
if(pc1==2):
    print()
    print("[•] Coloque a Quantidade de bits"), print()
    n3=int(input("> "))
    n4=n3//8
    print("[+]:Isso gera mais ou menos {} Bytes".format(n4))
if(pc1==3):
    print()
    print("[•] Coloque a Quantidade de Bytes"), print()
    n5=int(input("> "))
    n6=n5*8
    print("[+]: Isso gera {} bits".format(n6))
    
