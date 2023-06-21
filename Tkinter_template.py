import tkinter as tk
import tkinter.ttk as ttk
import random
from playsound import playsound
import os, sys
import time

#通常用
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("./audio")

#pyinstallerでexe化するとき用
#os.path.dirname((sys.executable))
#os.chdir("../")
#os.chdir("../audio")


class dnb_test():
    def __init__(self):
        self.rnd = []

    #ランダムな数字の要素を持つ配列を作る
    def random_make(self, digit):
        rnd = []
        for i in range(5):
            if i == 0:
                for i in range(digit):
                    rnd.append(random.randint(1,9))
            elif rnd == self.opp_arr(rnd):
                rnd = []
                for i in range(digit):
                    rnd.append(random.randint(1,9))
            else:
                break
        self.rnd = rnd

    #配列を逆順番にする
    def opp_arr(self, rnd):
        rnd_rvs=[]
        for i in range(len(rnd)-1,-1,-1):
            rnd_rvs.append(rnd[i])
        return rnd_rvs

    #インプットされた数字をlist型に変換する
    def input_arr(self, input_num):
        i = []
        while input_num > 0:
            i.append(input_num%10)
            input_num //= 10
        return self.opp_arr(i)

    #音を再生する
    def audio_play(self, file_num):
        file = str(file_num)+"num.wav"
        playsound(file)
        #time.sleep(0.5)

    #出題する
    def quest(self,digit):
        #配列生成
        self.random_make(digit)
        print(self.rnd)
        #音声再生
        for i in self.rnd:
            self.audio_play(i)

        return self.rnd
    
    def score(self, input, rnd):
        opp = self.opp_arr(rnd)
        if self.input_arr(input) == opp:
            text = "おめでとうございます！正解です"
            return text
        else:
            text = "残念。正解は" + str(opp)[1:-1] + "です"
            return text


class DesktopApp(tk.Frame, dnb_test):
# ==================================
# Applicationオブジェクトクラスの定義
# ==================================
#メインウィンドウ－－フレーム－－ウィジェット
#メインウィンドウ = tk.Tk()
# サブウィンドウ名 = tk.Toplevel(
# 背景色bg,ボーダーbd,カーソル指定cursor,ウィンドウの外観設定relief,高さheight,幅width)
#配置pack, grid, place
#pack : どこに寄せるかanchor(),親とサイズを合わせるexpand,スペースを埋めるfill,外隙間padx,pady
#       内隙間ipadx,ipady,つめる方向side
#grid : 配置する列column,何列にわたって配置するかcolumnspan,padx,pady,ipadx,ipady
#       配置する行row,何行にわたって配置するかrowspan,pack+anchor+fill=sticky
#place: 

    # ======================================
    # アプリケーションオブジェクト初期設定
    # ======================================
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        # ウィンドウの設定
        self.master.title("Tkinter test")    # タイトル
        self.master.geometry("600x400")     # サイズ

        # サイズ調整
        self.pack_propagate(0)

        # フレーム作成
        self.frame()
        # ウィジェット作成
        self.widgets()


    # ======================================
    # フレーム作成
    # ======================================

    #フレーム：Frame,Labelframe
    #フレーム名 = tk.Frame(親指定,幅width,高さheight,フレームの枠指定relief,背景色bg,ボーダーbd,
    #           マウスポインタの見た目cursor,枠とテキストとの間の縦の空白pady,横の空白padx
    #           Tabキーでのフォーカス移動の有無10)

    def frame(self):
        self.frame1 = tk.Frame(self.master,padx=10, pady=10, bg="#E6E6E6")
        self.frame1.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

        self.frame2 = tk.Frame(self.master,padx=10, pady=10, bg="#E6E6E6")
        self.frame2.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

        self.frame1.tkraise()   #最前面にする

    # ======================================
    # ウィジェット作成
    # ======================================

    #ウィジェット:文字Label,ボタン,Button,文字入力Entry,データ一覧表示Listbox,クリックでon/off切替Checkbutton,
    #           クリックでon/off切替Radiobutton,スライド調整Scale,文字列表示Message,プルダウン選択Combobox,
    #           アイテムをツリー表示Treeview,進捗状況表示Progressbar,Tab切替Notebook,調整可能なテキストボックスSpinbox
    #ウィジェット名 = tk.ウィジェット名(親指定,オプション)
    #Label = text,bg,bd,3D表示relief(flat,raised,sunken,groove,ridge),文字の色fg,font
    #button = text,command
    #entry = bg,bd,relief,textvariable,Entryに値を.set(),.get(),.delete()


    def widgets(self):
        option_pd1 = [3,4,5,6]
        self.pd1 = ttk.Combobox(self.frame1, height=4, width=5, justify="center", state="readonly", font=("Courier", 40, "bold"), cursor="arrow", values=option_pd1)
        self.pd1.set(3)
        self.pd1.pack(anchor=tk.N, pady=10)

        self.btn1 = tk.Button(self.frame1, text="スタート", command=lambda:self.btn_1(), font=("Courier", 40, "bold"))
        self.btn1.pack(anchor=tk.N, pady=10)

        self.label1 = tk.Label(self.frame1, text="", font=("Courier", 20, "bold"))
        self.label1.pack(anchor=tk.N, pady=10)
    
        self.label2 = tk.Label(self.frame2, text="", font=("Courier", 40, "bold"))
        self.label2.pack(anchor=tk.N, pady=10)

        self.vc = self.register(self.limit_char)
        self.entry1 = tk.Entry(self.frame2, width = 6, font=("Courier", 40, "bold"), validate="key", validatecommand=(self.vc, "%P"))
        self.entry1.bind('<Return>', self.enter)
        self.entry1.pack(anchor=tk.N, pady=10)


    # ======================================
    # イベント処理
    # ======================================
    def btn_1(self):
        self.frame2.tkraise()   #最前面にする
        self.label2["text"] = self.pd1.get()
        self.entry1.pack(anchor=tk.N, pady=10)
        self.entry1.focus_set()
        self.rnd = dnb_test().quest(int(self.pd1.get()))   #出題する
        

    def enter(self, event):
        self.label1["text"] = dnb_test().score(int(self.entry1.get()), self.rnd)
        self.entry1.delete(0, tk.END)
        self.frame1.tkraise()   #最前面にする
        

    #文字数制限
    def limit_char(self, string):
        return len(string) <= int(self.pd1.get())
    

# ==================================
# アプリケーション起動
# ==================================
if __name__=="__main__":
    root = tk.Tk()
    app = DesktopApp(master=root)
    app.mainloop()