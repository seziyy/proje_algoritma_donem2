while True:
    print("Menü Seçenekleri:")
    print("1. Seçenek : Sisteme Üye Ol")
    print("2. Seçenek : Sisteme Giriş Yap")
    print("3. Seçenek : Şifremi Unuttum")
    print("4. Çıkış")

    secim = input("Lütfen bir seçim yapın '1-4'): ")

    if secim == "1":
        while True:
            username = input("Kullanıcı adınızı oluşturun(tek haneli): ")
            if len(username) == 1:
                break
            else:
                print("Kullanıcı adı yalnızca tek haneli olmalıdır.")
        password = input("Şifrenizi girin: ")while True:
            print("Menü Seçenekleri:")
            print("1. Seçenek : Sisteme Üye Ol")
            print("2. Seçenek : Sisteme Giriş Yap")
            print("3. Seçenek : Şifremi Unuttum")
            print("4. Çıkış")

            secim = input("Lütfen bir seçim yapın '1-4'): ")

            if secim == "1":
                while True:
                    username = input("Kullanıcı adınızı oluşturun(tek haneli): ")
                    if len(username) == 1:
                        break
                    else:
                        print("Kullanıcı adı yalnızca tek haneli olmalıdır.")
                password = input("Şifrenizi girin: ")
                print("Şifreniz, büyük küçük harflere duyarlıdır.")

            elif secim == "2":
                print("Seçenek 2 seçildi.")
                kullaniciadi = "kullanıcı adı"
                sifre = "sifre"
                username = input("kullanıcı adı girin: ")
                password = input("şifrenizi girin: ")
                
                if username == kullaniciadi and password == sifre:
                    print("Giriş başarılı.")
                else:
                    print("Kullanıcı adı veya şifre yanlış.")
                    
            elif secim == "3":
                print("Seçenek 3 seçildi.")
                  
            elif secim == "4":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim! Lütfen tekrar deneyin.")
        print("Şifreniz, büyük küçük harflere duyarlıdır.")

    elif secim == "2":
        print("Seçenek 2 seçildi.")
        kullaniciadi = "kullanıcı adı"
        sifre = "sifre"
        username = input("kullanıcı adı girin: ")
        password = input("şifrenizi girin: ")
        
        if username == kullaniciadi and password == sifre:
            print("Giriş başarılı.")
        else:
            print("Kullanıcı adı veya şifre yanlış.")
            
    elif secim == "3":
        print("Seçenek 3 seçildi.")
          
    elif secim == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")