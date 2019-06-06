import sys
b = sys.modules.keys()
for i in range (len(b)):
	h=b[i]
	r=0
	for g in range(len(h)):
		if h[g] != '.':
			r=r+1
	if r==len(h):
		a=dir(__import__(b[i]))
		for y in range(len(a)):
			if a[y]=='GetMainCharacterIndex':
				playerm=b[i]
			if a[y]=='GetNameByVID':
				chrm=b[i]
			if a[y]=='SendShopEndPacket':
				netm=b[i]
			if a[y]=='SetGuildMarkPath':
				appm=b[i]
			if a[y]=='GetPrivateShopItemPrice':
				shopm=b[i]
			if a[y]=='Button':
				uim=b[i]
			if a[y]=='mouseController':
				mouseModulem=b[i]
			if a[y]=='AppendChat':
				chatm=b[i]
			if a[y]=='ClearSlot':
				wndMgrm=b[i]
			if a[y]=='GetCurrentMapName':
				backgroundm=b[i]
			if a[y]=='path' or 'exists' or 'path.exists':
				osm=b[i]
			if a[y]=='SetAffect':
				chrmgrm=b[i]
			if a[y]=='SelectItem':
				itemm=b[i]
			if a[y]=='ArrangeTextTail' or 'RegisterChatTail':
				textTailm=b[i]
			if a[y]=='ItemToolTip':
				uiToolTipm=b[i]
			if a[y]=='GetMonsterName' or 'GetLevelByVID' or 'GetGradeByVID':
				nonplayerm=b[i]
			if a[y]=='SelectAnswer':
				eventm=b[i]
			if a[y]=='ENVIRONMENT_NIGHT':
				constInfom=b[i]
			if a[y]=='floor' or 'fmod' or 'factorial':
				mathm=b[i]
			if a[y]=='GenerateColor':
				grpm=b[i]
			if a[y]=='clock' or 'clock_getres' or 'clock_gettime':
				timem=b[i]
huj='import '

try:
	import chr
except:
	exec (huj+chrm+' as chr')

try:
	import app
except:
	exec (huj+appm+' as app')

try:
	import shop
except:
	exec (huj+shopm+' as shop')

try:
	import playerm2g2 as player
	chr.GetPixelPosition = player.GetMainCharacterPosition
except:
	exec (huj+playerm+' as player')

try:
	import m2netm2g as net
except:
	exec (huj+netm+' as net')

try:
	import jebac_mh as ui
except:
	exec (huj+uim+' as ui')

try:
	import mouseModule
except:
	exec (huj+mouseModulem+' as mouseModule')

try:
	import chat
except:
	exec (huj+chatm+' as chat')

try:
	import wndMgr
except:
	exec (huj+wndMgrm+' as wndMgr')

try:
	import background
except:
	exec (huj+backgroundm+' as background')

try:
	import os
except:
	exec (huj+osm+' as os')

try:
	import chrmgr
except:
	exec (huj+chrmgrm+' as chrmgr')

try:
	import item
except:
	exec (huj+itemm+' as item')

try:
	import textTail
except:
	exec (huj+textTailm+' as textTail')

try:
	import uiToolTip
except:
	exec (huj+uiToolTipm+' as uiToolTip')

try:
	import nonplayer
except:
	exec (huj+nonplayerm+' as nonplayer')


try:
	import event
except:
	exec (huj+eventm+' as event')


try:
	import math
except:
	exec (huj+mathm+' as math')

try:
	import grp
except:
	exec (huj+grpm+' as grp')

try:
	import time
except:
	exec (huj+timem+' as time')

import dbg
ttt = 0
SPAM_HOTKEY_DOWN = TRUE
SPAM = TRUE
Czciaka = 'Tahoma:15'
BuffCzas = 0
targecik = 0
wykrywaczzero = 0
blogopoz = 1
pomocpoz = 1
odbiciepoz = 1
Position_Boss_X = 0
Position_Boss_Y = 0
Position_Metin_X = 0
Position_Metin_Y = 0
List=[]
dupa=[]
xxxx = 0
xoxx = 0
idii = 0
strona = 0
pozwolenieLISTY = 0
CURMAP = 0
TargetVid2=0
TargetVid=0
VidyPozwolenie=0
ListaVidow=[]
ListaVidow2=[]
Lista = []
autowtawanie_pozwo = 0
ks = 0
Mobber_ID = 0
Poty = 0
Poty_1_ID = 0
Poty_1_Icon = 0
Poty_2_ID = 0
Poty_2_Icon = 0
ListaRud = []
Otwieraczx = 0
Otwieracz_ID = [0,0,0,0,0,0,0,0,0]
Dopalaczx = 0
Otwieraczt = 0
Slotlista = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cfg = []
xox = 0
Dopalacz_ID = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
SlotUlepszania = 0
kostiumidx = 0
telestep = 0
teleport_mode = 0
listcord=[]
listash=[]
listakordy=[]
kukloma=0
cos=0
ch = 1
cipa = 0
costam=0
Egzo_ID =0
Rada_ID = 0
Ku_ID = 0
listakag=[]
listatypow = []
Pozwolenie = 0
met = 0
Odleglosc = 999999
Position_Metin_X = 0
Position_Metin_Y = 0
papec = 0
listash=[]
listash2=[]
listaWysz = []
SlotUlepszaniaDO = 0
Przyciskoff = '|cFFFF0000|Hitem|h'
Przyciskon =  '|cff00FF00|H|h'
Spambotp1 = ['|cffFFFFFF|H|hNormal', '|cFFFF0000|Hitem|hCzerwony','|cff00FF00|H|hZielony', '|cffFFFF00|H|hZolty', '|cFFFF00FF|Hitem|hRozowy', '|cFF804000|Hitem|hBrazowy','|cffffc700|Hitem|hZloty','|cff800080|H|hFiolotowy','|cFF0080FF|Hitem|hNiebieski','|cff00FFFF|H|hBlekitny']
bosy=[192,193,191,194,394,591,534,533,691,2191,1901,791,1304,2307,2206,2091]
rudy=('Zyla Diamentu','Zyla Bursztynu','Zyla Skamienialego Drewna','Zyla Miedzi','Zyla Srebra','Zyla Zlota','Zyla Jadelitu','Zyla Ebonitu','Zyla Sterta Muszli','Zyla Bialego Zlota','Zyla Krysztalu','Zyla Ametystu','Zyla Nieb. Lez','Wlasne Rudy')
rudy1 = ('Idz','Teleportuj')
Mobbercombo1 = ('Normal','Mega')
Autoaacombo1 = ('Normal','Rotacyjny')
GmComboList  = ('Informacja','Wyloguj','Wyjdz z gry')
UlepszanieComboText = ['Kowal','Kowal Gildyjny','Zwoj Blogoslawienstwa','Magiczny Metal','DT','Inne']
kordyx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
listazapisku = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
x = 0
COLOR_TEXT = {

}
Szukanie_metinow = 0
Szukanie_bosow = 0
Szukanie_gm = 0
def netSendChatPacket(text, type=0):
	global oldSendChatPacket, netSendChatPacket,Wlasna_ruda
	args = text.split(' ')
	args_count = len(args)-1


	if args[0] == '/info':
		chat.AppendChat(2, 'Multihack by Montes')
		chat.AppendChat(2, 'www.worldofmetin.pl')
	elif args[0]=='/loadpy':
		if args_count==1:
			import os
			if os.path.exists(args[1]):
				app.RunPythonFile(args[1])
	elif args[0]=='/z':
		app.SetCameraMaxDistance(100000)
	elif args[0]=='/Fix_Shop':
		shop.GetOfflineShopItemPrice=shop.GetItemPrice
		shop.GetOfflineShopItemCount=shop.GetItemCount
		shop.GetOfflineShopItemID=shop.GetItemID
		shop.IsOfflineShop=shop.IsPrivateShop
		shop.OFFLINE_SHOP_SLOT_COUNT=shop.SHOP_SLOT_COUNT
		net.SendOfflineShopEndPacket=net.SendShopEndPacket


	else:
		for color, color2 in COLOR_TEXT.items():
			text = text.replace(color, color2)
		oldSendChatPacket(text,type)

oldSendChatPacket = net.SendChatPacket
net.SendChatPacket = netSendChatPacket
chat.AppendChat(8, 'Multihack by Montes')
chat.AppendChat(8, '/info - Informacje')
chat.AppendChat(8, 'Pobrano z www.worldofmetin.pl')


def uno(aa):
	return aa[6]

abc = 0

import x7ArS5dKf
def pulok():
	for i in xrange(shop.OFFLINE_SHOP_SLOT_COUNT):
		if shop.GetOfflineShopItemPrice(i)>0:
			return 1
		if i==(shop.OFFLINE_SHOP_SLOT_COUNT)-1:
			return 0
def DivideToFloat1(x, y):
	try:
		return x * (y**-1)
	except:
		return 0
class Dialog1(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()
		self.Zmianakoloru()
		self.uuuiii()
		state = 'stop'
		try:
			self.Krzycz()
			self.Krzycz1()
			self.WczytajFarmCord()
			self.Loadfff()

		except:
			pass
		self.itemlist = {}
		self.itemlist1 = {}

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Board1 = ui.Bar()
		self.Board1.SetSize(223,230)
		self.Board1.SetCenterPosition()
		self.Board1.AddFlag('movable')
		self.Board1.AddFlag('float')
		self.Board1.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.0))
		self.Board1.Show()

		self.Boardinne = ui.Board()
		self.Boardinne.SetParent(self.Board1)
		self.Boardinne.SetSize(115, 200)
		self.Boardinne.SetPosition(320, 15)
		self.Boardinne.Hide()

		self.Boarddod = ui.Board()
		self.Boarddod.SetParent(self.Board1)
		self.Boarddod.SetSize(125, 200)
		self.Boarddod.SetPosition(210, 15)
		self.Boarddod.Hide()

		self.Board = ui.BoardWithTitleBar()
		self.Board.SetParent(self.Board1)
		self.Board.SetSize(223,235)
		self.Board.SetPosition(0, 0)
		self.Board.SetTitleName('Worldofmetin.pl - Montes')
		self.Board.SetCloseEvent(self.Close)
		self.Board.Show()


		self.Auto_Attack_img = ui.ExpandedImageBox()
		self.Auto_Attack_img.SetParent(self)
		self.Auto_Attack_img.SetPosition(2, wndMgr.GetScreenHeight()-150)
		self.Auto_Attack_img.LoadImage('banner.tga')
		self.Auto_Attack_img.Show()

		self.WykrywaczOkno = ui.BoardWithTitleBar()
		self.WykrywaczOkno.SetSize(470, 165)
		self.WykrywaczOkno.SetCenterPosition()
		self.WykrywaczOkno.AddFlag('movable')
		self.WykrywaczOkno.AddFlag('float')
		self.WykrywaczOkno.SetTitleName('Wykrywacz')
		self.WykrywaczOkno.SetCloseEvent(self.CloseWykr)
		self.WykrywaczOkno.Hide()

		self.DopalaczeOknoBoard = ui.BoardWithTitleBar()
		self.DopalaczeOknoBoard.SetSize(270, 210)
		self.DopalaczeOknoBoard.SetCenterPosition()
		self.DopalaczeOknoBoard.AddFlag('movable')
		self.DopalaczeOknoBoard.AddFlag('float')
		self.DopalaczeOknoBoard.SetTitleName('Dopalacze')
		self.DopalaczeOknoBoard.SetCloseEvent(self.CloseDopy)
		self.DopalaczeOknoBoard.Hide()

		self.Spambotboard = ui.BoardWithTitleBar()
		self.Spambotboard.SetSize(437, 208)
		self.Spambotboard.SetCenterPosition()
		self.Spambotboard.AddFlag('movable')
		self.Spambotboard.AddFlag('float')
		self.Spambotboard.SetTitleName('Spambot')
		self.Spambotboard.SetCloseEvent(self.Spambotclose)
		self.Spambotboard.Hide()

		self.Ustawieniao = ui.BoardWithTitleBar()
		self.Ustawieniao.SetSize(390, 195)
		self.Ustawieniao.SetCenterPosition()
		self.Ustawieniao.AddFlag('movable')
		self.Ustawieniao.AddFlag('float')
		self.Ustawieniao.SetTitleName('Ustawienia')
		self.Ustawieniao.SetCloseEvent(self.Ustawieniaoclose)
		self.Ustawieniao.Hide()

		self.OtwieraczBoard = ui.BoardWithTitleBar()
		self.OtwieraczBoard.SetSize(255, 155)
		self.OtwieraczBoard.SetCenterPosition()
		self.OtwieraczBoard.AddFlag('movable')
		self.OtwieraczBoard.AddFlag('float')
		self.OtwieraczBoard.SetTitleName('Otwieracz')
		self.OtwieraczBoard.SetCloseEvent(self.OtwieraczBoardclose)
		self.OtwieraczBoard.Hide()

		self.Typstr = ui.BoardWithTitleBar()
		self.Typstr.SetSize(150, 280)
		self.Typstr.SetCenterPosition()
		self.Typstr.AddFlag('movable')
		self.Typstr.AddFlag('float')
		self.Typstr.SetTitleName('Typ Bicia')
		self.Typstr.SetCloseEvent(self.Typstrclose)
		self.Typstr.Hide()

		self.UlepszBoard = ui.BoardWithTitleBar()
		self.UlepszBoard.SetSize(175, 146)
		self.UlepszBoard.SetCenterPosition()
		self.UlepszBoard.AddFlag('movable')
		self.UlepszBoard.AddFlag('float')
		self.UlepszBoard.SetTitleName('Ulepszanie')
		self.UlepszBoard.SetCloseEvent(self.CloseUlepsz)
		self.UlepszBoard.Hide()

		self.Pogoda = ui.BoardWithTitleBar()
		self.Pogoda.SetSize(120, 190)
		self.Pogoda.SetCenterPosition()
		self.Pogoda.AddFlag('movable')
		self.Pogoda.AddFlag('float')
		self.Pogoda.SetTitleName('Pogoda')
		self.Pogoda.SetCloseEvent(self.ClosePogoda)
		self.Pogoda.Hide()

		self.AutoSkileBoard = ui.BoardWithTitleBar()
		self.AutoSkileBoard.SetSize(150, 120)
		self.AutoSkileBoard.SetCenterPosition()
		self.AutoSkileBoard.AddFlag('movable')
		self.AutoSkileBoard.AddFlag('float')
		self.AutoSkileBoard.SetTitleName('Skill Bot')
		self.AutoSkileBoard.SetCloseEvent(self.AutoSkileClose)
		self.AutoSkileBoard.Hide()

		self.BoardPickup = ui.BoardWithTitleBar()
		self.BoardPickup.SetSize(170, 220)
		self.BoardPickup.SetCenterPosition()
		self.BoardPickup.AddFlag('movable')
		self.BoardPickup.AddFlag('float')
		self.BoardPickup.SetTitleName('Pickup')
		self.BoardPickup.SetCloseEvent(self.ClosePickup)
		self.ciul=[]
		self.BoardPickup.Hide()

		self.BoardPickupInfo = ui.BoardWithTitleBar()
		self.BoardPickupInfo.SetSize(360, 80)
		self.BoardPickupInfo.SetCenterPosition()
		self.BoardPickupInfo.AddFlag('float')
		self.BoardPickupInfo.SetTitleName('Info')
		self.BoardPickupInfo.SetCloseEvent(self.ClosePickupInfo)
		self.ciul=[]
		self.BoardPickupInfo.Hide()

		self.BoardInfo = ui.BoardWithTitleBar()
		self.BoardInfo.SetSize(260, 140)
		self.BoardInfo.SetCenterPosition()
		self.BoardInfo.AddFlag('movable')
		self.BoardInfo.AddFlag('float')
		self.BoardInfo.SetTitleName('About')
		self.BoardInfo.SetCloseEvent(self.CloseInfo)
		self.BoardInfo.Hide()

		self.BoardInfoBossy = ui.BoardWithTitleBar()
		self.BoardInfoBossy.SetSize(260, 150)
		self.BoardInfoBossy.SetCenterPosition()
		self.BoardInfoBossy.AddFlag('movable')
		self.BoardInfoBossy.AddFlag('float')
		self.BoardInfoBossy.SetTitleName('Bossy Ustawienia')
		self.BoardInfoBossy.SetCloseEvent(self.CloseInfoBossy)
		self.BoardInfoBossy.Hide()

		self.BoardInfoKopacz = ui.BoardWithTitleBar()
		self.BoardInfoKopacz.SetSize(260, 150)
		self.BoardInfoKopacz.SetCenterPosition()
		self.BoardInfoKopacz.AddFlag('movable')
		self.BoardInfoKopacz.AddFlag('float')
		self.BoardInfoKopacz.SetTitleName('Kopacz Rud Ustawienia')
		self.BoardInfoKopacz.SetCloseEvent(self.CloseInfoKopacz)
		self.BoardInfoKopacz.Hide()

		self.BoardKopacz = ui.BoardWithTitleBar()
		self.BoardKopacz.SetSize(170, 170)
		self.BoardKopacz.SetCenterPosition()
		self.BoardKopacz.AddFlag('movable')
		self.BoardKopacz.AddFlag('float')
		self.BoardKopacz.SetTitleName('Kopacz Rud')
		self.BoardKopacz.SetCloseEvent(self.CloseKopacz)
		self.BoardKopacz.Hide()

		self.BoardRozdzielanie = ui.BoardWithTitleBar()
		self.BoardRozdzielanie.SetSize(190, 100)
		self.BoardRozdzielanie.SetCenterPosition()
		self.BoardRozdzielanie.AddFlag('movable')
		self.BoardRozdzielanie.AddFlag('float')
		self.BoardRozdzielanie.SetTitleName('Rozdzielanie')
		self.BoardRozdzielanie.SetCloseEvent(self.CloseRozdzielanie)
		self.BoardRozdzielanie.Hide()

		self.BoardGildia = ui.BoardWithTitleBar()
		self.BoardGildia.SetSize(140, 120)
		self.BoardGildia.SetCenterPosition()
		self.BoardGildia.AddFlag('movable')
		self.BoardGildia.AddFlag('float')
		self.BoardGildia.SetTitleName('Gildia Funkcje')
		self.BoardGildia.SetCloseEvent(self.CloseGildia)
		self.BoardGildia.Hide()

		self.ShopScannerBoard = ui.BoardWithTitleBar()
		self.ShopScannerBoard.SetSize(400, 513)
		self.ShopScannerBoard.SetCenterPosition()
		self.ShopScannerBoard.AddFlag('movable')
		self.ShopScannerBoard.AddFlag('float')
		self.ShopScannerBoard.SetTitleName('Shop Scanner')
		self.ShopScannerBoard.SetCloseEvent(self.CloseShopScanner)
		self.ShopScannerBoard.Hide()

		self.BoardCzyelnika = ui.BoardWithTitleBar()
		self.BoardCzyelnika.SetSize(240, 190)
		self.BoardCzyelnika.SetCenterPosition()
		self.BoardCzyelnika.AddFlag('movable')
		self.BoardCzyelnika.AddFlag('float')
		self.BoardCzyelnika.SetTitleName('Czytanie KU')
		self.BoardCzyelnika.SetCloseEvent(self.CloseCzytajnik)
		self.BoardCzyelnika.Hide()

		self.BoardBuffbot = ui.BoardWithTitleBar()
		self.BoardBuffbot.SetSize(150, 160)
		self.BoardBuffbot.SetCenterPosition()
		self.BoardBuffbot.AddFlag('movable')
		self.BoardBuffbot.AddFlag('float')
		self.BoardBuffbot.SetTitleName('Buff Bot')
		self.BoardBuffbot.SetCloseEvent(self.CloseBuffbot)
		self.BoardBuffbot.Hide()

		self.BoardAutoMetin = ui.BoardWithTitleBar()
		self.BoardAutoMetin.SetSize(340, 130)
		self.BoardAutoMetin.SetCenterPosition()
		self.BoardAutoMetin.AddFlag('movable')
		self.BoardAutoMetin.AddFlag('float')
		self.BoardAutoMetin.SetTitleName('Auto Bicie Metinow')
		self.BoardAutoMetin.SetCloseEvent(self.CloseAutoMetin)
		self.BoardAutoMetin.Hide()

		self.BoardStatusPlus = ui.BoardWithTitleBar()
		self.BoardStatusPlus.SetSize(165, 150)
		self.BoardStatusPlus.SetCenterPosition()
		self.BoardStatusPlus.AddFlag('movable')
		self.BoardStatusPlus.AddFlag('float')
		self.BoardStatusPlus.SetTitleName('Dodawanie Statystyk')
		self.BoardStatusPlus.SetCloseEvent(self.CloseStatusPlus)
		self.BoardStatusPlus.Hide()

		self.BoardZap = ui.BoardWithTitleBar()
		self.BoardZap.SetSize(670, 137)
		self.BoardZap.SetCenterPosition()
		self.BoardZap.AddFlag('movable')
		self.BoardZap.AddFlag('float')
		self.BoardZap.SetTitleName('Zapis pozycji')
		self.BoardZap.SetCloseEvent(self.CloseZap)
		self.BoardZap.Hide()

		self.BoardMetin = ui.Board()
		self.BoardMetin.SetSize(205, 70)
		self.BoardMetin.SetPosition(1, wndMgr.GetScreenHeight()/2-(wndMgr.GetScreenHeight()/8))
		self.BoardMetin.AddFlag('float')
		self.BoardMetin.Hide()

		self.BoardBoss = ui.Board()
		self.BoardBoss.SetSize(205, 70)
		self.BoardBoss.SetPosition(1, wndMgr.GetScreenHeight()/2-(wndMgr.GetScreenHeight()/8)+68)
		self.BoardBoss.AddFlag('float')
		self.BoardBoss.Hide()

		self.BoardLow = ui.BoardWithTitleBar()
		self.BoardLow.SetSize(150, 100)
		self.BoardLow.SetCenterPosition()
		self.BoardLow.AddFlag('movable')
		self.BoardLow.AddFlag('float')
		self.BoardLow.SetTitleName('Fishbot')
		self.BoardLow.SetCloseEvent(self.CloseLow)
		self.BoardLow.Hide()

		self.BoardLow1 = ui.BoardWithTitleBar()
		self.BoardLow1.SetSize(125, 445)
		self.BoardLow1.SetCenterPosition()
		self.BoardLow1.AddFlag('movable')
		self.BoardLow1.AddFlag('float')
		self.BoardLow1.SetTitleName('Czas wedki')
		self.BoardLow1.SetCloseEvent(self.CloseLowInfo)
		self.BoardLow1.Hide()

		self.Board19 = ui.Bar()
		self.Board19.SetSize(wndMgr.GetScreenWidth(), 15)
		self.Board19.SetPosition(0,0)
		self.Board19.AddFlag('float')
		self.Board19.SetColor(grp.GenerateColor(0.5, 0.5, 0.5,0.3))
		self.Board19.Show()

		self.BoardNew = ui.BoardWithTitleBar()
		self.BoardNew.SetSize(155, 83)
		self.BoardNew.SetCenterPosition()
		self.BoardNew.AddFlag('movable')
		self.BoardNew.AddFlag('float')
		self.BoardNew.SetTitleName('Damage hack')
		self.BoardNew.SetCloseEvent(self.CloseNew)
		self.BoardNew.Hide()

		self.comp = Component()
		self.Spambotp = self.comp.ComboBox(self.Spambotboard, 'Kolor', 20, 160, 70)
		for Spambotp in Spambotp1:
			self.Spambotp.InsertItem(1,str(Spambotp))

		self.Rozdajpele = self.comp.SlotbarText(self.Ustawieniao, 'Rodziaj pelerynek', 255, 35, 115, 15)
		self.Rozdajautoataczku = self.comp.SlotbarText(self.Ustawieniao, 'Rodziaj auto ataku', 255, 90, 115, 15)
		self.RozdajWykrywaczaGM = self.comp.SlotbarText(self.Ustawieniao, 'Rodziaj wykrywacza GM', 255, 145, 115, 15)

		self.Rudzisze = self.comp.ComboBox(self.BoardKopacz, 'Rudy', 15, 120, 140)
		for Rudzisze in rudy:
			self.Rudzisze.InsertItem(1,str(Rudzisze))

		self.Rudzisze1 = self.comp.ComboBox(self.BoardKopacz, 'Teleportuj', 15, 140, 140)
		for Rudzisze1 in rudy1:
			self.Rudzisze1.InsertItem(1,str(Rudzisze1))

		self.Mobbercombo = self.comp.ComboBox(self.Ustawieniao, 'Normal', 255, 55, 115)
		for Mobbercombo in Mobbercombo1:
			self.Mobbercombo.InsertItem(1,str(Mobbercombo))

		self.Autoaacombo = self.comp.ComboBox(self.Ustawieniao, 'Normal', 255,110, 115)
		for Autoaacombo in Autoaacombo1:
			self.Autoaacombo.InsertItem(1,str(Autoaacombo))

		self.GmCombo = self.comp.ComboBox(self.Ustawieniao, 'Informacja', 255,165, 115)
		for GmCombo in GmComboList:
			self.GmCombo.InsertItem(1,str(GmCombo))

		self.Zapcombo = self.comp.ComboBox(self.BoardZap, 'Nr. Zapisu', 31, 100, 85)
		for Zapcombo in listazapisku:
			self.Zapcombo.InsertItem(1,str(Zapcombo))

		self.UlepszanieCombo = self.comp.ComboBox(self.UlepszBoard, 'Typ', 50, 120, 110)
		for UlepszanieCombo in UlepszanieComboText:
			self.UlepszanieCombo.InsertItem(1,str(UlepszanieCombo))

		self.PokazWiecej = self.comp.Button(self.Board, ' ', '', 200, 33, self.Wiecej, 'd:/ymir work/ui/game/windows/btn_plus_up.sub', 'd:/ymir work/ui/game/windows/btn_plus_over.sub', 'd:/ymir work/ui/game/windows/btn_plus_down.sub')
		self.SchowajWiecej = self.comp.Button(self.Board, ' ', '', 200, 47, self.Mniej, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')

		self.PokazWiecej1 = self.comp.Button(self.Boarddod, ' ', '', 103, 33, self.Wiecej1, 'd:/ymir work/ui/game/windows/btn_plus_up.sub', 'd:/ymir work/ui/game/windows/btn_plus_over.sub', 'd:/ymir work/ui/game/windows/btn_plus_down.sub')
		self.SchowajWiecej1 = self.comp.Button(self.Boarddod, ' ', '', 103, 47, self.Mniej1, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')

		self.btns3 = ui.Button()
		self.btns3.SetPosition(3, wndMgr.GetScreenHeight()/2-wndMgr.GetScreenHeight()/10)
		self.btns3.SetEvent(self.OpenWindow)
		self.btns3.SetUpVisual('d:/ymir work/ui/game/windows/tab_button_large_01.sub')
		self.btns3.SetOverVisual('d:/ymir work/ui/game/windows/tab_button_large_02.sub')
		self.btns3.SetDownVisual('d:/ymir work/ui/game/windows/tab_button_large_03.sub')
		self.btns3.SetText('Pokaz Okno Mh')
		self.btns3.Hide()


		self.Skan = ui.ToggleButton()
		self.Skan.SetParent(self.ShopScannerBoard)
		self.Skan.SetPosition(13, 56)
		self.Skan.SetUpVisual('d:/ymir work/ui/public/xlarge_button_01.sub')
		self.Skan.SetOverVisual('d:/ymir work/ui/public/xlarge_button_02.sub')
		self.Skan.SetDownVisual('d:/ymir work/ui/public/xlarge_button_03.sub')
		self.Skan.SetToggleUpEvent(ui.__mem_func__(self.autopotystopfunkcja))
		self.Skan.SetToggleDownEvent(ui.__mem_func__(self.PotyStartFunc1))
		self.Skan.SetText('Skanuj')
		self.Skan.Show()

		self.linieexec = ui.SlotBar()
		self.linieexec.SetParent(self.ShopScannerBoard)
		self.linieexec.SetSize(367, 17)
		self.linieexec.SetPosition(14, 34)
		self.linieexec.Show()
		self.liniecos=ui.EditLine()
		self.liniecos.SetParent(self.linieexec)
		self.liniecos.SetSize(367, 17)
		self.liniecos.SetPosition(1, 1)
		self.liniecos.SetMax(70)
		self.liniecos.SetLimitWidth(300)
		self.liniecos.SetMultiLine()
		self.liniecos.SetText('')
		self.liniecos.Show()

		self.button = ui.Button()
		self.button.SetParent(self.ShopScannerBoard)
		self.button.SetPosition(203,56)
		self.button.SetUpVisual('d:/ymir work/ui/public/xlarge_button_01.sub')
		self.button.SetOverVisual('d:/ymir work/ui/public/xlarge_button_01.sub')
		self.button.SetDownVisual('d:/ymir work/ui/public/xlarge_button_01.sub')
		self.button.SetText('Wyszukaj Przedmiot')
		self.button.Show()
		self.button.SetEvent(self.autopotystopfunkcja)
		self.shopscaninfo = self.comp.Button(self.ShopScannerBoard, '', 'Jesli nie dziala kliknij', 20, 9, self.ooo, 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_01.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_02.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_03.sub')

		self.Waznepick = self.comp.TextLine(self.BoardPickupInfo, 'Aby dodac item do listy kliknij Dodaj Item gdy lezy na ziemi', 15, 35, self.comp.RGB(71, 131, 255),Czciaka)
		self.Waznepick1 = self.comp.TextLine(self.BoardPickupInfo, 'Przedmionty nie sa podnoszone gdy gra jest zminimalizowana', 15, 50, self.comp.RGB(71, 131, 255),Czciaka)



		self.TylCzytajki = self.comp.ThinBoard(self.BoardCzyelnika, FALSE, 175, 35, 50, 130, FALSE)

		self.Rozdzieltyl = self.comp.ThinBoard(self.BoardRozdzielanie, FALSE, 20, 35, 50, 50, FALSE)
		self.Rozdziel = self.comp.Button(self.BoardRozdzielanie, 'Rozdziel', '', 90, 60, self.Rozdziel_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.slotbar_PoIleRozdzielicIn, self.PoIleRozdzielicIn = self.comp.EditLine(self.BoardRozdzielanie, '15', 155, 35, 18, 15, 5)
		self.PoIlerozdzielictxt = self.comp.SlotbarText(self.BoardRozdzielanie, 'Po ile podzielic', 75, 35, 82, 15)
		self.bar_Pickupselect, self.list_Pickupselect = self.comp.ListBoxEx(self.BoardPickup, 110, 30, 50, 150,7 ,self)
		self.DodajItem = self.comp.Button(self.BoardPickup, 'Dodaj Item', '', 15, 100, self.DodajItem_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.UsunItem = self.comp.Button(self.BoardPickup, 'Usun Item', '', 15, 130, self.UsunItem_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.InfoPickup = self.comp.Button(self.BoardPickup, 'Info', '', 60, 190, self.OpenWindowPickupInfo, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.pickupn = self.comp.ToggleButton(self.BoardPickup, 'Normal Pickup', '', 15, 160, (lambda arg = 'off': self.pickupn_func(arg)), (lambda arg = 'on': self.pickupn_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.pickall = self.comp.ToggleButton(self.BoardPickup, 'Pick Wszystko', '', 15, 40, (lambda arg = 'off': self.pickall_func(arg)), (lambda arg = 'on': self.pickall_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.pickwyb = self.comp.ToggleButton(self.BoardPickup, 'Pick Wybrane', '', 15, 70, (lambda arg = 'off': self.pickwyb_func(arg)), (lambda arg = 'on': self.pickwyb_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Waznepick0 = self.comp.TextLine(self.BoardPickup, 'Wazne', 15, 190, self.comp.RGB(255, 0, 0),Czciaka)

		self.Zoom = self.comp.Button(self.Pogoda, 'Zoom', '', 15, 80, self.Zoom_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Dzien = self.comp.Button(self.Pogoda, 'Dzien', '', 15, 30, self.Dzien_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Ghost = self.comp.Button(self.Pogoda, 'Ghost', '', 15, 130, self.Ghost_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Noc = self.comp.Button(self.Pogoda, 'Noc', '', 15, 55, self.Noc_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Snieg = self.comp.ToggleButton(self.Pogoda, 'Snieg', '', 15, 105, (lambda arg = 'off': self.Snieg_func(arg)), (lambda arg = 'on': self.Snieg_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Kamera = self.comp.ToggleButton(self.Pogoda, 'Zatrzymaj kamere', '', 15, 155, (lambda arg = 'off': self.Kamera_func(arg)), (lambda arg = 'on': self.Kamera_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')

		self.Info = self.comp.Button(self.Board, '', '', 20, 9, self.OpenWindowInfo, 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_01.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_02.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_03.sub')
		self.Gora = self.comp.Button(self.Board, 'Gora', '', 134, 135, self.Gora_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Lewo = self.comp.Button(self.Board, 'Lewo', '', 113, 155, self.Lewo_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Prawo = self.comp.Button(self.Board, 'Prawo', '', 155, 155, self.Prawo_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Dol = self.comp.Button(self.Board, 'Dol', '', 134, 175, self.Dol_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Tpdokordow = self.comp.Button(self.Board, 'Tp do kordow', '', 15, 200, self.Tpdokordow_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Zamknijgre = self.comp.Button(self.Board, 'Zamknij Gre', '', 110, 200, self.Zamknijgre_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Pickup = self.comp.Button(self.Board, 'Pickup', '', 15, 55, self.OpenWindowPickup, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.AutoAtak = self.comp.ToggleButton(self.Board, 'Auto Atak', '', 15, 30, (lambda arg = 'off': self.AutoAtak_func(arg)), (lambda arg = 'on': self.AutoAtak_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Mobberek = self.comp.ToggleButton(self.Board, 'Mobber', '', 110, 30, (lambda arg = 'off': self.Mobber_func(arg)), (lambda arg = 'on': self.Mobber_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Dopalacze = self.comp.ToggleButton(self.Board, 'Dopalacze', '', 15, 80, (lambda arg = 'off': self.Dopalacze_func(arg)), (lambda arg = 'on': self.Dopalacze_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Poty = self.comp.ToggleButton(self.Board, 'Auto Poty', '', 110, 55, (lambda arg = 'off': self.Poty_func(arg)), (lambda arg = 'on': self.Poty_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Otwieracz = self.comp.Button(self.Board, 'Otwieracz', '', 110, 105, self.OpenWindowOtwieraczBoard, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.AutoWstawanie = self.comp.ToggleButton(self.Board, 'Auto Wstawanie', '', 110, 80, (lambda arg = 'off': self.AutoWstawanie_func(arg)), (lambda arg = 'on': self.AutoWstawanie_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.WykrywaczGM = self.comp.ToggleButton(self.Board, 'Wykrywacz GM', '', 15, 105, (lambda arg = 'off': self.WykrywaczGM_func(arg)), (lambda arg = 'on': self.WykrywaczGM_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		#self.CrashMap = self.comp.ToggleButton(self.Board, 'Crash map', '', 15, 130, (lambda arg = 'off': self.Crashmap_func(arg)), (lambda arg = 'on': self.Crashmap_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.boardneeeew = self.comp.Button(self.Board, 'Damage hack', '', 15, 130, self.OpenWindowNew, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')

		self.WaitHack = self.comp.ToggleButton(self.BoardNew, 'WaitHack', '', 57, 30, (lambda arg = 'off': self.WaitHack_func(arg)), (lambda arg = 'on': self.WaitHack_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.AtakNaCel = self.comp.ToggleButton(self.BoardNew, 'Atak Na Cel', '', 57, 52, (lambda arg = 'off': self.WaitHack_func1(arg)), (lambda arg = 'on': self.WaitHack_func1(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.slotbar_Whspeed, self.Whspeed = self.comp.EditLine(self.BoardNew, '0.1', 20, 35, 30, 15, 8)
		self.slotbar_ACspeed, self.ACspeed = self.comp.EditLine(self.BoardNew, '0.1', 20, 55, 30, 15, 8)
		self.slotbar_Xin, self.Xin = self.comp.EditLine(self.Board, '', 62, 156, 30, 15, 4)
		self.slotbar_Yin, self.Yin = self.comp.EditLine(self.Board, '', 62, 177, 30, 15, 4)
		self.Podajx = self.comp.TextLine(self.Board, 'Podaj X:', 15, 157, self.comp.RGB(255, 255, 0),Czciaka)
		self.Podajy = self.comp.TextLine(self.Board, 'Podaj Y:', 15, 177, self.comp.RGB(255, 255, 0),Czciaka)

		self.AutoSkilestr = self.comp.Button(self.Boarddod, 'Auto Skile', '', 15, 10, self.AutoSkileWindow, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.WykrywaczMetinow = self.comp.Button(self.Boarddod, 'Wykrywacz', '', 15, 30, self.OpenWindowWykr, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Dopalaczestr = self.comp.Button(self.Boarddod, 'Dopalacze', '', 15, 50, self.OpenWindowDopy, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Spambot = self.comp.Button(self.Boarddod, 'Spam Bot', '', 15, 70, self.OpenWindowSpam, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Ustawienia = self.comp.Button(self.Boarddod, 'Ustawienia', '', 15, 90, self.OpenWindowUstawieniao, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.KopaczrudStr = self.comp.Button(self.Boarddod, 'Kopacz Rud', '', 15, 110, self.OpenWindowKopacz, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.ShopScannerstr = self.comp.Button(self.Boarddod, 'Shop Scanner', '', 15, 130, self.OpenWindowShopScanner, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Zapispozycjistr = self.comp.Button(self.Boarddod, 'Zapis Pozycji', '', 15, 150, self.OpenWindowZap, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Buffbotx = self.comp.Button(self.Boarddod, 'Buff Bot', '', 15, 170, self.OpenWindowBuffbot, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')

		self.Czytaniestr = self.comp.Button(self.Boardinne, 'Czytanie KU', '', 15, 10, self.OpenWindowCzytajnik, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Pogodastr = self.comp.Button(self.Boardinne, 'Pogoda', '', 15, 30, self.OpenWindowPogoda, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Dodawaniestatx = self.comp.Button(self.Boardinne, 'Dodaw. Statystyk', '', 15, 50, self.OpenWindowStatusPlus, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.RozdzielanieStr = self.comp.Button(self.Boardinne, 'Rozdzielanie', '', 15, 70, self.OpenWindowRozdzielanie, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.GildiaStr = self.comp.Button(self.Boardinne, 'Gildia', '', 15, 90, self.OpenWindowGildia, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Fishbotstr = self.comp.Button(self.Boardinne, 'Fishbot', '', 15, 110, self.OpenWindowLow, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Ulepszanie = self.comp.Button(self.Boardinne, 'Ulepszanie', '', 15, 130, self.OpenWindowUlepsz, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.ZapisUstaw = self.comp.Button(self.Boardinne, 'Zapisz Ustawienia', '', 15, 170, self.ZapiszUstawienia, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.WczytajUstaw = self.comp.Button(self.Boardinne, 'Wczytaj Ustawienia', '', 15, 150, self.WczytajUstawienia, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')


		self.SzukajMetinow = self.comp.ToggleButton(self.WykrywaczOkno, 'Szukaj', '', 31, 110, (lambda arg = 'off': self.SzukajMetinow_func(arg)), (lambda arg = 'on': self.SzukajMetinow_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tpdometina = self.comp.Button(self.WykrywaczOkno, 'Teleportuj', '', 121, 110, self.WykrywaczMetinowFuncStartx, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.SzukajBossow= self.comp.ToggleButton(self.WykrywaczOkno, 'Szukaj', '', 261, 110, (lambda arg = 'off': self.SzukajBossow_func(arg)), (lambda arg = 'on': self.SzukajBossow_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.TpdoBossa = self.comp.Button(self.WykrywaczOkno, 'Teleportuj', '', 351, 110, self.WykrywaczBossowFuncStartx, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Autometinx = self.comp.Button(self.WykrywaczOkno, 'Auto Metin', '', 190, 135, self.OpenWindowAutoMetin, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Nazwametina = self.comp.SlotbarText(self.WykrywaczOkno, 'Nazwa Metina:', 20, 40, 80, 18)
		self.Pozycjametinax = self.comp.SlotbarText(self.WykrywaczOkno, 'Pozycja x:', 20, 62, 80, 18)
		self.Pozycjametinay = self.comp.SlotbarText(self.WykrywaczOkno, 'Pozycja y:', 20, 84, 80, 18)
		self.Nazwabossa = self.comp.SlotbarText(self.WykrywaczOkno, 'Nazwa Bossa:', 250, 40, 80, 18)
		self.Pozycjabossax = self.comp.SlotbarText(self.WykrywaczOkno, 'Pozycja x:', 250, 62, 80, 18)
		self.Pozycjabossay123 = self.comp.SlotbarText(self.WykrywaczOkno, 'Pozycja y:', 250, 84, 80, 18)
		self.Nazwametina2, self.Nazwametina2x = self.comp.SlotbarText(self.WykrywaczOkno, '', 110, 40, 110, 18)
		self.Pozycjametinax2, self.Pozycjametinax2x = self.comp.SlotbarText(self.WykrywaczOkno, '', 110, 62, 110, 18)
		self.Pozycjametinay2, self.Pozycjametinay2x = self.comp.SlotbarText(self.WykrywaczOkno, '', 110, 84, 110, 18)
		self.Nazwabossa2, self.Nazwabossa2x  = self.comp.SlotbarText(self.WykrywaczOkno, '', 340, 40, 110, 18)
		self.Pozycjabossax2, self.Pozycjabossax2x = self.comp.SlotbarText(self.WykrywaczOkno, '', 340, 62, 110, 18)
		self.Pozycjabossay2, self.Pozycjabossay2x = self.comp.SlotbarText(self.WykrywaczOkno, '', 340, 84, 110, 18)
		self.slotbar_KopaczBossy, self.BossyInfo = self.comp.EditLine(self.BoardInfoBossy, '', 25, 35, 210, 50, 180)
		self.DodajBossa = self.comp.Button(self.BoardInfoBossy, 'Dodaj Bossa', '', 85, 90, self.DodajBossa_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Bossyinfox1 = self.comp.TextLine(self.BoardInfoBossy, 'Aby dodac bossa zaznacz go i kliknij Dodaj Bossa', 20, 115, self.comp.RGB(255, 255, 0),'Tahoma:13')
		self.Bossyinfox10 = self.comp.Button(self.WykrywaczOkno, '', '', 20, 9, self.OpenWindowInfoBossy, 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_01.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_02.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_03.sub')

		self.NazwametinaBok = self.comp.TextLine(self.BoardMetin, 'Nazwa Metina:', 17, 15, self.comp.RGB(255, 255, 0),Czciaka)
		self.MetinZamknij = self.comp.Button(self.BoardMetin, 'Zamknij', '', 105, 35, self.CloseMetinOkno, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.TpDoMetinaBok = self.comp.Button(self.BoardMetin, 'Tp do metina', '', 15, 35, self.WykrywaczMetinowFuncStartx, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.NazwabossaBok = self.comp.TextLine(self.BoardBoss, 'Nazwa Bossa:', 17, 15, self.comp.RGB(255, 255, 0),Czciaka)
		self.BossZamknij = self.comp.Button(self.BoardBoss, 'Zamknij', '', 105, 35, self.CloseBossOkno, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tpdobossabok = self.comp.Button(self.BoardBoss, 'Tp do Bossa', '', 15, 35, self.WykrywaczBossowFuncStartx, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')

		self.Coiledopy1 = self.comp.SlotbarText(self.DopalaczeOknoBoard, 'Co ile min uzywac dopalaczy', 15, 180, 220, 15)
		self.slotbar_Coiledopyin, self.Coiledopyin = self.comp.EditLine(self.DopalaczeOknoBoard, '10', 231, 180, 25, 15, 3)
		self.dsds = self.comp.ThinBoard(self.DopalaczeOknoBoard, FALSE, 10, 33, 245, 145, FALSE)
		self.gives = ui.GridSlotWindow()
		self.gives.SetParent(self.DopalaczeOknoBoard)
		self.gives.SetPosition(20, 40)
		self.gives.ArrangeSlot(1, 7, 4, 32, 32, 0, 0)
		self.gives.SetSlotBaseImage('d:/ymir work/ui/public/Slot_Base.sub', 1.0, 1.0, 1.0, 1.0)
		self.gives.Show()
		self.gives.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		self.usundopybtn = self.comp.Button(self.DopalaczeOknoBoard, ' ', '', 249, 50, self.usundopy, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')

		self.tylpotki = self.comp.ThinBoard(self.Ustawieniao, FALSE, 195, 40, 50, 130, FALSE)
		self.slotbar_Potyhpczas, self.Potyhpczas = self.comp.EditLine(self.Ustawieniao, '90', 170, 57, 20, 15, 2)
		self.slotbar_Potympczas, self.Potympczas = self.comp.EditLine(self.Ustawieniao, '90', 170, 97, 20, 15, 2)
		self.slotbar_Peleczas, self.Peleczas = self.comp.EditLine(self.Ustawieniao, '5', 170, 137, 20, 15, 3)
		self.odilepotyhp = self.comp.SlotbarText(self.Ustawieniao, 'Od ilu % HP uzywac potek', 20, 57, 150, 15)
		self.odilepotymp = self.comp.SlotbarText(self.Ustawieniao, 'Od ilu % MP uzywac potek', 20, 97, 150, 15)
		self.coilepele = self.comp.SlotbarText(self.Ustawieniao, 'Co ilywac peleryn', 20, 137, 150, 15)


		self.Tyl = self.comp.ThinBoard(self.Spambotboard, FALSE, 13, 32, 410, 109, FALSE)
		self.Spambtn = self.comp.ToggleButton(self.Spambotboard, 'Normal', '', 190, 158, (lambda arg = 'off': self.Spambtn_func(arg)), (lambda arg = 'on': self.Spambtn_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Spambtn1 = self.comp.ToggleButton(self.Spambotboard, 'Wolaj', '', 96, 158, (lambda arg = 'off': self.Spambtn_func1(arg)), (lambda arg = 'on': self.Spambtn_func1(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.slotbar_Tekstin, self.Tekstin = self.comp.EditLine(self.Spambotboard, 'Wprowadz tekst...', 25, 45, 385, 75, 37500)
		self.slotbar_Coilespamtxtin, self.Coilespamtxtin = self.comp.EditLine(self.Spambotboard, '15', 385, 159, 20, 15, 3)
		self.Coilespambotin = self.comp.SlotbarText(self.Spambotboard, 'Co ile sekund pisac', 290, 159, 95, 15)

		self.slotbar_Dopyczas, self.Dopyczas = self.comp.EditLine(self.OtwieraczBoard, '0.1', 217, 55, 20, 15, 4)
		self.coiledopy1hhhff = self.comp.SlotbarText(self.OtwieraczBoard, 'Co ile otwierac', 132, 55, 85, 15)
		self.tylotwiwracz = self.comp.ThinBoard(self.OtwieraczBoard, FALSE, 15, 35, 107, 107, FALSE)
		self.Otwieraj = self.comp.ToggleButton(self.OtwieraczBoard, 'Otwieraj', '', 141, 90, (lambda arg = 'off': self.Otwieracz_func(arg)), (lambda arg = 'on': self.Otwieracz_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.gives1 = ui.GridSlotWindow()
		self.gives1.SetParent(self.OtwieraczBoard)
		self.gives1.SetPosition(20, 40)
		self.gives1.ArrangeSlot(1, 3, 3, 32, 32, 0, 0)
		self.gives1.SetSlotBaseImage('d:/ymir work/ui/public/Slot_Base.sub', 1.0, 1.0, 1.0, 1.0)
		self.gives1.Show()
		self.gives1.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot1))
		self.usunotwbtn = self.comp.Button(self.OtwieraczBoard, ' ', '', 125, 35, self.usunotw, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')

		self.Ulepsz = self.comp.Button(self.UlepszBoard, 'Ulepsz', '', 65, 58, self.Ulepsz_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.slotbar_Oileulepszycin, self.Oileulepszycin = self.comp.EditLine(self.UlepszBoard, '9', 140, 35, 16, 16, 5)
		self.Oiletxt = self.comp.SlotbarText(self.UlepszBoard, 'O ile ulepszyc', 57, 35, 82, 16)


		self.Aurax1 = self.comp.ExpandedImage(self.AutoSkileBoard, 20, 40, 'd:/ymir work/ui/skill/warrior/geomgyeong_03.sub')
		self.Berekx1 = self.comp.ExpandedImage(self.AutoSkileBoard, 60, 40, 'd:/ymir work/ui/skill/warrior/jeongwi_03.sub')
		self.Silnex1 = self.comp.ExpandedImage(self.AutoSkileBoard, 20, 40, 'd:/ymir work/ui/skill/warrior/cheongeun_03.sub')
		self.Ostrzex1 = self.comp.ExpandedImage(self.AutoSkileBoard, 60, 40, 'd:/ymir work/ui/skill/sura/gwigeom_03.sub')
		self.Strachx1 = self.comp.ExpandedImage(self.AutoSkileBoard, 20, 40, 'd:/ymir work/ui/skill/sura/gongpo_03.sub')
		self.Zbrojax1 = self.comp.ExpandedImage(self.AutoSkileBoard, 100, 40, 'd:/ymir work/ui/skill/sura/jumagap_03.sub')
		self.Ochronkax1 = self.comp.ExpandedImage(self.AutoSkileBoard, 20, 40, 'd:/ymir work/ui/skill/sura/heuksin_03.sub')
		self.Duchx1 = self.comp.ExpandedImage(self.AutoSkileBoard, 60, 40, 'd:/ymir work/ui/skill/sura/muyeong_03.sub')
		self.Atakx1 = self.comp.ExpandedImage(self.AutoSkileBoard, 20, 40, 'd:/ymir work/ui/skill/shaman/jeungryeok_03.sub')
		self.Zwinnoscx1 = self.comp.ExpandedImage(self.AutoSkileBoard, 60, 40, 'd:/ymir work/ui/skill/shaman/kwaesok_03.sub')
		self.Blogox1 = self.comp.ExpandedImage(self.AutoSkileBoard, 20, 40, 'd:/ymir work/ui/skill/shaman/hosin_03.sub')
		self.Pomocx1 = self.comp.ExpandedImage(self.AutoSkileBoard, 60, 40, 'd:/ymir work/ui/skill/shaman/gicheon_03.sub')
		self.Odbiciex1 = self.comp.ExpandedImage(self.AutoSkileBoard, 100, 40, 'd:/ymir work/ui/skill/shaman/boho_03.sub')

		self.Aurax = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 20, 40, (lambda arg = 'off': self.Skill4Buff_func(arg)), (lambda arg = 'on': self.Skill4Buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Berekx = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 60, 40, (lambda arg = 'off': self.Skill3Buff_func(arg)), (lambda arg = 'on': self.Skill3Buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Silnex = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 20, 40, (lambda arg = 'off': self.Skill4Buff_func(arg)), (lambda arg = 'on': self.Skill4Buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Ostrzex = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 60, 40, (lambda arg = 'off': self.Skill3Buff_func(arg)), (lambda arg = 'on': self.Skill3Buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Strachx = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 20, 40, (lambda arg = 'off': self.Skill4Buff_func(arg)), (lambda arg = 'on': self.Skill4Buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Zbrojax = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 100, 40, (lambda arg = 'off': self.Skill5buff_func(arg)), (lambda arg = 'on': self.Skill5buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Ochronkax = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 20, 40, (lambda arg = 'off': self.Skill4Buff_func(arg)), (lambda arg = 'on': self.Skill4Buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Duchx = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 60, 40, (lambda arg = 'off': self.Skill3Buff_func(arg)), (lambda arg = 'on': self.Skill3Buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Atakx = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 20, 40, (lambda arg = 'off': self.Skill6buff_func(arg)), (lambda arg = 'on': self.Skill6buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Zwinnoscx = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 60, 40, (lambda arg = 'off': self.Skill5buff_func(arg)), (lambda arg = 'on': self.Skill5buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Blogox = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 20, 40, (lambda arg = 'off': self.Skill4Buff_func(arg)), (lambda arg = 'on': self.Skill4Buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Pomocx = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 60, 40, (lambda arg = 'off': self.Skill6buff_func1(arg)), (lambda arg = 'on': self.Skill6buff_func1(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.Odbiciex = self.comp.ToggleButton(self.AutoSkileBoard, '', '', 100, 40, (lambda arg = 'off': self.Skill5buff_func(arg)), (lambda arg = 'on': self.Skill5buff_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.slotbar_Skill1czas, self.Skill1czas = self.comp.EditLine(self.AutoSkileBoard, '120', 23, 75, 25, 15, 3)
		self.slotbar_Skill2czas, self.Skill2czas = self.comp.EditLine(self.AutoSkileBoard, '83', 63, 75, 25, 15, 3)
		self.slotbar_Skill3czas, self.Skill3czas = self.comp.EditLine(self.AutoSkileBoard, '45', 103, 75, 25, 15, 3)

		self.Czytaj = self.comp.ToggleButton(self.BoardCzyelnika, 'Czytaj', '',45, 150, (lambda arg = 'off': self.Czytaj_func(arg)), (lambda arg = 'on': self.Czytaj_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Wstawradetxt = self.comp.SlotbarText(self.BoardCzyelnika, 'Wstaw Rade Pustelnika:', 10, 47, 150, 15)
		self.wstawegzotxt = self.comp.SlotbarText(self.BoardCzyelnika, 'Wstaw Zwoj Egzorcyzmu:', 10, 87, 150, 15)
		self.wstawkutxt = self.comp.SlotbarText(self.BoardCzyelnika, 'Wstaw Ksi\\xeage Umiejetno\\x9cci:', 10, 127, 150, 15)

		self.InfoKopacz = self.comp.Button(self.BoardKopacz, '', '', 20, 9, self.OpenWindowInfoKopacz, 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_01.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_02.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_03.sub')
		self.Idz_do_rudy = self.comp.Button(self.BoardKopacz, 'Idz do rudy', '', 40, 35, self.Idz_do_rudy_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Kop_rude = self.comp.ToggleButton(self.BoardKopacz, 'Kop rude', '', 40, 65, (lambda arg = 'off': self.Kop_rude_func(arg)), (lambda arg = 'on': self.Kop_rude_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.kopaczczas = self.comp.SlotbarText(self.BoardKopacz, 'Podaj co ile kopac', 15, 90, 118, 15)
		self.slotbar_Kopacz, self.Kopacztime = self.comp.EditLine(self.BoardKopacz, '30', 133, 90, 20, 15, 4)
		self.slotbar_KopaczInfo, self.KopaczInfo = self.comp.EditLine(self.BoardInfoKopacz, '', 25, 35, 210, 50, 180)
		self.DodajRude = self.comp.Button(self.BoardInfoKopacz, 'Dodaj Rude', '', 85, 90, self.DodajRude_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.kopaczczas1 = self.comp.TextLine(self.BoardInfoKopacz, 'Aby dodac rude zaznacz ja i kliknij Dodaj Rude', 20, 115, self.comp.RGB(255, 255, 0),'Tahoma:13')

		self.OddawajExpBtn = self.comp.ToggleButton(self.BoardGildia, 'Oddawaj Expa', '', 25, 35, (lambda arg = 'off': self.OddExpGildia_func(arg)), (lambda arg = 'on': self.OddExpGildia_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.slotbar_NazwagildicIn, self.NazwagildicIn = self.comp.EditLine(self.BoardGildia, 'Nazwa Gildii', 15, 65, 110, 15, 15)
		self.Zalozgildiebtn = self.comp.Button(self.BoardGildia, 'Zaloz Gildie', '', 25, 90, self.zrobgildie, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')

		self.BlogoBuffBot1 = self.comp.ExpandedImage(self.BoardBuffbot, 20, 60, 'd:/ymir work/ui/skill/shaman/hosin_03.sub')
		self.PomocBuffBot1 = self.comp.ExpandedImage(self.BoardBuffbot, 60, 60, 'd:/ymir work/ui/skill/shaman/gicheon_03.sub')
		self.OdbicieBuffBot1 = self.comp.ExpandedImage(self.BoardBuffbot, 100, 60, 'd:/ymir work/ui/skill/shaman/boho_03.sub')
		self.BlogoBuffBot = self.comp.ToggleButton(self.BoardBuffbot, '', '', 20, 60, (lambda arg = 'off': self.BlogoBuffBot_func(arg)), (lambda arg = 'on': self.BlogoBuffBot_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.PomocBuffBot = self.comp.ToggleButton(self.BoardBuffbot, '', '', 60, 60, (lambda arg = 'off': self.PomocBuffBot_func(arg)), (lambda arg = 'on': self.PomocBuffBot_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.OdbicieBuffBot = self.comp.ToggleButton(self.BoardBuffbot, '', '', 100, 60, (lambda arg = 'off': self.OdbicieBuffBot_func(arg)), (lambda arg = 'on': self.OdbicieBuffBot_func(arg)), 'd:/ymir work/ui/public/slot_cover_button_01.sub', 'd:/ymir work/ui/public/slot_cover_button_02.sub', 'd:/ymir work/ui/public/slot_cover_button_03.sub')
		self.ZatwCelu = self.comp.Button(self.BoardBuffbot, 'Zatwierdz Cel', '', 32.5, 100, self.ZatwCelu_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.StartBuffBot = self.comp.ToggleButton(self.BoardBuffbot, 'Start', '', 32.5, 125, (lambda arg = 'off': self.StartBuffBot_func(arg)), (lambda arg = 'on': self.StartBuffBot_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.CelBuff = self.comp.TextLine(self.BoardBuffbot, 'Cel -', 20, 40, self.comp.RGB(255, 255, 0),Czciaka)

		self.pos = 0
		self.dodajkordytn = self.comp.Button(self.BoardAutoMetin, 'Dodaj Pozycje', '', 20, 70, self.Dodaj_Kordy_Do_Listy, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.slotbar_kordyinmet, self.kordyinmet = self.comp.EditLine(self.BoardAutoMetin, '', 125, 41, 200, 70, 9)
		self.pokazmetbtn = self.comp.Button(self.BoardAutoMetin, '', '', 110, 44, self.ShowMetinKordy, 'd:/ymir work/ui/game/windows/btn_plus_up.sub', 'd:/ymir work/ui/game/windows/btn_plus_over.sub', 'd:/ymir work/ui/game/windows/btn_plus_down.sub')
		self.chowajmetbtn = self.comp.Button(self.BoardAutoMetin, '', '', 110, 74, self.HideMetinKordy, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')
		self.tpiszukaj = self.comp.ToggleButton(self.BoardAutoMetin, 'Tp i szukaj', '', 20, 40, (lambda arg = 'off': self.Tpiszukaj_func(arg)), (lambda arg = 'on': self.Tpiszukaj_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.PozycjaText = self.comp.TextLine(self.BoardAutoMetin, 'Pozycja 0 / 0', 21,96,self.comp.RGB(255, 255, 0),Czciaka)

		self.Witplus = self.comp.Button(self.BoardStatusPlus, 'Dodaj Wit', '', 55, 37, self.Witplus_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Intplus = self.comp.Button(self.BoardStatusPlus, 'Dodaj Int', '', 55, 62, self.Intplus_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Silaplus = self.comp.Button(self.BoardStatusPlus, 'Dodaj Si\\xb3e', '', 55, 87, self.Silaplus_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Zreplus = self.comp.Button(self.BoardStatusPlus, 'Dodaj Zre', '', 55, 112, self.Zreplus_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.slotbar_Witin, self.Witin = self.comp.EditLine(self.BoardStatusPlus, '10', 25, 40, 25, 15, 3)
		self.slotbar_Intin, self.Intin = self.comp.EditLine(self.BoardStatusPlus, '10', 25, 65, 25, 15, 3)
		self.slotbar_Silain, self.Silain = self.comp.EditLine(self.BoardStatusPlus, '10', 25, 90, 25, 15, 3)
		self.slotbar_Zrein, self.Zrein = self.comp.EditLine(self.BoardStatusPlus, '10', 25, 115, 25, 15, 3)

		self.Zapisz = self.comp.Button(self.BoardZap, 'Zapisz', '', 30, 40, self.Zapisz_funcZap, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp1 = self.comp.Button(self.BoardZap, '1', '', 142, 40, self.Tp1_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp2 = self.comp.Button(self.BoardZap, '2', '', 142, 70, self.Tp2_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp3 = self.comp.Button(self.BoardZap, '3', '', 142, 100, self.Tp3_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp4 = self.comp.Button(self.BoardZap, '4', '', 242, 40, self.Tp4_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp5 = self.comp.Button(self.BoardZap, '5', '', 242, 70, self.Tp5_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp6 = self.comp.Button(self.BoardZap, '6', '', 242, 100, self.Tp6_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp7 = self.comp.Button(self.BoardZap, '7', '', 342, 40, self.Tp7_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp8 = self.comp.Button(self.BoardZap, '8', '', 342, 70, self.Tp8_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp9 = self.comp.Button(self.BoardZap, '9', '', 342, 100, self.Tp9_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp10 = self.comp.Button(self.BoardZap, '10', '', 442, 40, self.Tp10_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp11 = self.comp.Button(self.BoardZap, '11', '', 442, 70, self.Tp11_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp12 = self.comp.Button(self.BoardZap, '12', '', 442, 100, self.Tp12_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp13 = self.comp.Button(self.BoardZap, '13', '', 542, 40, self.Tp13_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp14 = self.comp.Button(self.BoardZap, '14', '', 542, 70, self.Tp14_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Tp15 = self.comp.Button(self.BoardZap, '15', '', 542, 100, self.Tp15_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.slotbar_edit973, self.NazwaZapisu = self.comp.EditLine(self.BoardZap, 'Nazwa', 31, 70, 85, 15, 30)

		self.MpcMontes = self.comp.Button(self.BoardInfo, 'Mpc', '', 30, 55, self.MpcMontes_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.MpcMontes = self.comp.Button(self.BoardInfo, 'Mpc', '', 100, 100, self.MpcKag_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.YTMontes = self.comp.Button(self.BoardInfo, 'YT', '', 100, 55, self.YTMontes_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.GGMontes = self.comp.Button(self.BoardInfo, 'GG', '', 170, 55, self.GGMontes_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.Multibcinfo = self.comp.TextLine(self.BoardInfo, 'Multihack by Montes', 80, 30, self.comp.RGB(0, 192, 255),Czciaka)
		self.Multispkag = self.comp.TextLine(self.BoardInfo, 'Pickup, ShopScanner By Montes', 45, 80, self.comp.RGB(223, 129, 83),Czciaka)


		self.LowRybkinoobku = self.comp.ToggleButton(self.BoardLow, 'Low ryby', '', 33, 60, (lambda arg = 'off': self.lowienie_func(arg)), (lambda arg = 'on': self.lowienie_func(arg)), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.fISHINFOX = self.comp.Button(self.BoardLow, '', '', 20, 9, self.OpenWindowInfoLow, 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_01.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_02.sub', 'd:/ymir work/ui/game/taskbar/Open_Chat_Log_Button_03.sub')
		self.slotbar_lowienieczas, self.lowienieczas = self.comp.EditLine(self.BoardLow, '2.85', 110, 35, 25, 15, 15)
		self.Pozycjabossay2hh, self.Pozycjabossay2xhhhh = self.comp.SlotbarText(self.BoardLow, 'Czowienia', 20, 35, 85, 15)
		self.Czaslowieniap, self.Czaslowieniapx = self.comp.SlotbarText(self.BoardLow1, 'Wedka +1 - 2.85', 20, 35, 85, 15)
		self.Czaslowieniap1, self.Czaslowieniapx1 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +2 - 2.80', 20, 55, 85, 15)
		self.Czaslowieniap2, self.Czaslowieniapx2 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +3 - 2.75', 20, 75, 85, 15)
		self.Czaslowieniap3, self.Czaslowieniapx3 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +4 - 2.65', 20, 95, 85, 15)
		self.Czaslowieniap4, self.Czaslowieniapx4 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +5 - 2.65', 20, 115, 85, 15)
		self.Czaslowieniap5, self.Czaslowieniapx5 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +6 - 2.65', 20, 135, 85, 15)
		self.Czaslowieniap6, self.Czaslowieniapx6 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +7 - 2.65', 20, 155, 85, 15)
		self.Czaslowieniap7, self.Czaslowieniapx7 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +8 - 2.60', 20, 175, 85, 15)
		self.Czaslowieniap8, self.Czaslowieniapx8 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +9 - 2.60', 20, 195, 85, 15)
		self.Czaslowieniap9, self.Czaslowieniapx9 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +10 - 2.45', 20, 215, 85, 15)
		self.Czaslowieniap10, self.Czaslowieniapx10 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +11 - 2.40', 20, 235, 85, 15)
		self.Czaslowieniap11, self.Czaslowieniapx11 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +12 - 2.35', 20, 255, 85, 15)
		self.Czaslowieniap12, self.Czaslowieniapx12 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +13 - 2.30', 20, 275, 85, 15)
		self.Czaslowieniap13, self.Czaslowieniapx13 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +14 - 2.25', 20, 295, 85, 15)
		self.Czaslowieniap14, self.Czaslowieniapx14 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +15 - 2.17', 20, 315, 85, 15)
		self.Czaslowieniap15, self.Czaslowieniapx15 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +16 - 2.05', 20, 335, 85, 15)
		self.Czaslowieniap16, self.Czaslowieniapx16 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +17 - 1.95', 20, 355, 85, 15)
		self.Czaslowieniap17, self.Czaslowieniapx17 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +18 - 1.85', 20, 375, 85, 15)
		self.Czaslowieniap18, self.Czaslowieniapx18 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +19 - 1.75', 20, 395, 85, 15)
		self.Czaslowieniap19, self.Czaslowieniapx19 = self.comp.SlotbarText(self.BoardLow1, 'Wedka +20 - 1.57', 20, 415, 85, 15)

		self.MobberSlot = ui.ExpandedImageBox()
		self.MobberSlot.SetParent(self.tylpotki)
		self.MobberSlot.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.MobberSlot.OnMouseLeftButtonUp = lambda: self.MobberSlotFunc()
		self.MobberSlot.OnMouseRightButtonUp = lambda: self.usunpele()
		self.MobberSlot.SetPosition(9,89)
		self.MobberSlot.Show()

		self.MobberSlotIcon = ui.ExpandedImageBox()
		self.MobberSlotIcon.SetParent(self.tylpotki)
		self.MobberSlotIcon.SetPosition(9,89)
		self.MobberSlotIcon.LoadImage('')
		self.MobberSlotIcon.OnMouseLeftButtonUp = lambda: self.MobberSlotFunc()
		self.MobberSlot.OnMouseRightButtonUp = lambda: self.usunpele()
		self.MobberSlotIcon.Show()

		self.PotySlot = ui.ExpandedImageBox()
		self.PotySlot.SetParent(self.tylpotki)
		self.PotySlot.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.PotySlot.OnMouseLeftButtonUp = lambda: self.Set_Poty_1_ID()
		self.PotySlot.OnMouseRightButtonUp = lambda: self.usunpotehp()
		self.PotySlot.SetPosition(9,5)
		self.PotySlot.Show()

		self.PotySlotIcon = ui.ExpandedImageBox()
		self.PotySlotIcon.SetParent(self.tylpotki)
		self.PotySlotIcon.SetPosition(9,5)
		self.PotySlotIcon.OnMouseLeftButtonUp = lambda: self.Set_Poty_1_ID()
		self.PotySlotIcon.OnMouseRightButtonUp = lambda: self.usunpotehp()
		self.PotySlotIcon.Show()

		self.PotySlot2 = ui.ExpandedImageBox()
		self.PotySlot2.SetParent(self.tylpotki)
		self.PotySlot2.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.PotySlot2.OnMouseLeftButtonUp = lambda: self.Set_Poty_2_ID()
		self.PotySlot2.OnMouseRightButtonUp = lambda: self.usunpotemp()
		self.PotySlot2.SetPosition(9,47)
		self.PotySlot2.Show()

		self.PotySlotIcon2 = ui.ExpandedImageBox()
		self.PotySlotIcon2.SetParent(self.tylpotki)
		self.PotySlotIcon2.SetPosition(9,47)
		self.PotySlotIcon2.OnMouseLeftButtonUp = lambda: self.Set_Poty_2_ID()
		self.PotySlotIcon2.OnMouseRightButtonUp = lambda: self.usunpotemp()
		self.PotySlotIcon2.Show()

		self.UlepszanieSlot1 = ui.ExpandedImageBox()
		self.UlepszanieSlot1.SetParent(self.UlepszBoard)
		self.UlepszanieSlot1.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.UlepszanieSlot1.OnMouseLeftButtonUp = lambda: self.Ulepsz_Item()
		self.UlepszanieSlot1.SetPosition(15,30)
		self.UlepszanieSlot1.Show()

		self.UlepszanieSlot2 = ui.ExpandedImageBox()
		self.UlepszanieSlot2.SetParent(self.UlepszBoard)
		self.UlepszanieSlot2.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.UlepszanieSlot2.OnMouseLeftButtonUp = lambda: self.Ulepsz_Item()
		self.UlepszanieSlot2.SetPosition(15,62)
		self.UlepszanieSlot2.Show()

		self.UlepszanieSlot3 = ui.ExpandedImageBox()
		self.UlepszanieSlot3.SetParent(self.UlepszBoard)
		self.UlepszanieSlot3.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.UlepszanieSlot3.OnMouseLeftButtonUp = lambda: self.Ulepsz_Item()
		self.UlepszanieSlot3.SetPosition(15,94)
		self.UlepszanieSlot3.Show()

		self.UlepszanieSlotIcon = ui.ExpandedImageBox()
		self.UlepszanieSlotIcon.SetParent(self.UlepszBoard)
		self.UlepszanieSlotIcon.SetPosition(15,30)
		self.UlepszanieSlotIcon.LoadImage('')
		self.UlepszanieSlotIcon.OnMouseLeftButtonUp = lambda: self.Ulepsz_Item()
		self.UlepszanieSlotIcon.Show()

		self.UlepszanieSlot3x = ui.ExpandedImageBox()
		self.UlepszanieSlot3x.SetParent(self.UlepszBoard)
		self.UlepszanieSlot3x.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.UlepszanieSlot3x.OnMouseLeftButtonUp = lambda: self.SlotUleDo()
		self.UlepszanieSlot3x.SetPosition(89,82)
		self.UlepszanieSlot3x.Show()

		self.UlepszanieSlotIconx = ui.ExpandedImageBox()
		self.UlepszanieSlotIconx.SetParent(self.UlepszBoard)
		self.UlepszanieSlotIconx.SetPosition(89,82)
		self.UlepszanieSlotIconx.LoadImage('')
		self.UlepszanieSlotIconx.OnMouseLeftButtonUp = lambda: self.SlotUleDo()
		self.UlepszanieSlotIconx.Show()

		self.RozdzielanieSlot = ui.ExpandedImageBox()
		self.RozdzielanieSlot.SetParent(self.Rozdzieltyl)
		self.RozdzielanieSlot.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.RozdzielanieSlot.OnMouseLeftButtonUp = lambda: self.Set_Rozdzielanie_Slot()
		self.RozdzielanieSlot.SetPosition(8,8)
		self.RozdzielanieSlot.Show()

		self.RozdzielanieSlotIcon = ui.ExpandedImageBox()
		self.RozdzielanieSlotIcon.SetParent(self.RozdzielanieSlot)
		self.RozdzielanieSlotIcon.SetPosition(0,0)
		self.RozdzielanieSlotIcon.LoadImage('')
		self.RozdzielanieSlotIcon.OnMouseLeftButtonUp = lambda: self.Set_Rozdzielanie_Slot()
		self.RozdzielanieSlotIcon.Show()

		self.RadySlot = ui.ExpandedImageBox()
		self.RadySlot.SetParent(self.TylCzytajki)
		self.RadySlot.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.RadySlot.OnMouseLeftButtonUp = lambda: self.RadySlotFunc()
		self.RadySlot.OnMouseRightButtonUp = lambda: self.usunrade()
		self.RadySlot.SetPosition(9,5)
		self.RadySlot.Show()

		self.RadySlotIcon = ui.ExpandedImageBox()
		self.RadySlotIcon.SetParent(self.TylCzytajki)
		self.RadySlotIcon.SetPosition(9,5)
		self.RadySlotIcon.LoadImage('')
		self.RadySlotIcon.OnMouseLeftButtonUp = lambda: self.RadySlotFunc()
		self.RadySlotIcon.OnMouseRightButtonUp = lambda: self.usunrade()
		self.RadySlotIcon.Show()

		self.EgzoSlot = ui.ExpandedImageBox()
		self.EgzoSlot.SetParent(self.TylCzytajki)
		self.EgzoSlot.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.EgzoSlot.OnMouseLeftButtonUp = lambda: self.EgzoSlotFunc()
		self.EgzoSlot.OnMouseRightButtonUp = lambda: self.usunegzo()
		self.EgzoSlot.SetPosition(9,47)
		self.EgzoSlot.Show()

		self.EgzoSlotIcon = ui.ExpandedImageBox()
		self.EgzoSlotIcon.SetParent(self.TylCzytajki)
		self.EgzoSlotIcon.SetPosition(9,47)
		self.EgzoSlotIcon.OnMouseLeftButtonUp = lambda: self.EgzoSlotFunc()
		self.EgzoSlotIcon.OnMouseRightButtonUp = lambda: self.usunegzo()
		self.EgzoSlotIcon.Show()

		self.KUSlot = ui.ExpandedImageBox()
		self.KUSlot.SetParent(self.TylCzytajki)
		self.KUSlot.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
		self.KUSlot.OnMouseLeftButtonUp = lambda: self.KuSlotFunc()
		self.KUSlot.OnMouseRightButtonUp = lambda: self.usunku()
		self.KUSlot.SetPosition(9,89)
		self.KUSlot.Show()

		self.KUSloticon = ui.ExpandedImageBox()
		self.KUSloticon.SetParent(self.TylCzytajki)
		self.KUSloticon.SetPosition(9,89)
		self.KUSloticon.OnMouseLeftButtonUp = lambda: self.KuSlotFunc()
		self.KUSloticon.OnMouseRightButtonUp = lambda: self.usunku()
		self.KUSloticon.Show()


	def WaitHack_func(self, arg):
		if arg=='on':
			self.waithackStart()
			self.WaitHack.SetText(Przyciskon+'WaitHack')
		elif arg=='off':
			self.waithackStop()
			self.WaitHack.SetText(Przyciskoff+'WaitHack')

	def waithackStart(self):
		global listash2,VidyPozwolenie

		for i in listash2:
			dystans = player.GetCharacterDistance(i)
			if dystans > 0 and dystans < 1500:
				x7ArS5dKf.qsHg7JdL(i)
		self.waithackti=XX()
		self.waithackti.XX1(float(self.Whspeed.GetText()))
		self.waithackti.XX2(self.waithackStart)

	def waithackStop(self):
		self.waithackti=XX()
		self.waithackti.XX1(float(9999999999999))
		self.waithackti.XX2(self.waithackStart)

	def WaitHack_func1(self, arg):
		if arg=='on':
			self.waithackStart1()
			self.AtakNaCel.SetText(Przyciskon+'Atak na cel')
		elif arg=='off':
			self.waithackStop1()
			self.AtakNaCel.SetText(Przyciskoff+'Atak na cel')

	def waithackStart1(self):
		x7ArS5dKf.qsHg7JdL(int(player.GetTargetVID()))
		self.waithackti1=XX()
		self.waithackti1.XX1(float(self.ACspeed.GetText()))
		self.waithackti1.XX2(self.waithackStart1)

	def waithackStop1(self):
		self.waithackti1=XX()
		self.waithackti1.XX1(float(9999999999999))
		self.waithackti1.XX2(self.waithackStart1)


	def DivideToFloat(self,x, y):
		try:
			return x * (y**-1)
		except:
			return 0

	def Zmianakoloru(self):
		global abc
		if abc>=wndMgr.GetScreenWidth():
			abc=0
		abc+=1

		if os.path.isfile('banner.tga'):
			pass
		else:
			#dbg.LogBox('Brak banner.tga')
			pass#app.Exit()
		self.Wordlofmetin1.SetPosition(abc, 1)
		self.kolorkiz1=XX()
		self.kolorkiz1.XX1(0.01)
		self.kolorkiz1.XX2(self.Zmianakoloru)

	def GetTmpTeleport(self,DestX, DestY):
		global DivideToFloat
		(PlayerX, PlayerY, PlayerZ) = player.GetMainCharacterPosition()
		DifX = DestX - PlayerX
		DifY = DestY - PlayerY
		Vektor = self.DivideToFloat(2000, math.sqrt(DifX**2 + DifY**2))
		TempX = PlayerX + Vektor*DifX
		TempY = PlayerY + Vektor*DifY
		Count = self.DivideToFloat((DestX - PlayerX), (Vektor*DifX))
		return (TempX, TempY, Count)

	def Debug(self):
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

	def TeleportToDest(self,aimx, aimy):
		global Debug, GetTmpTeleport, TeleportState
		(TmpX, TmpY, Count) = self.GetTmpTeleport(aimx, aimy)
		TmpCount = 0
		myVid = player.GetMainCharacterIndex()
		while TmpCount < Count:
			chr.SelectInstance(myVid)
			(TmpX, TmpY, Crap) = self.GetTmpTeleport(aimx, aimy)
			chr.SetPixelPosition(int(TmpX), int(TmpY))
			TmpCount += 1
			self.Debug()

		chr.SetPixelPosition(int(aimx), int(aimy))
		self.Debug()
		TeleportState = 1
		chr.SelectInstance(myVid)

	def Wiecej(self):
		self.Boarddod.Show()
		self.Board1.SetSize(325,230)

	def Mniej(self):
		self.Boarddod.Hide()
		self.Boardinne.Hide()
		self.Board1.SetSize(230,230)

	def Wiecej1(self):
		self.Boardinne.Show()
		self.Board1.SetSize(435,230)

	def Mniej1(self):
		self.Boardinne.Hide()
		self.Board1.SetSize(325,230)

	def ZmianaCH(self):
		global ch
		if ch == 1:
			ch = 5
		else:
			ch = 1
		oldSendChatPacket(str('/ch ')+str(ch))

	def Zoom_func(self):
		self.zoom=XX()
		self.zoom.XX1(1)
		self.zoom.XX2(self.Zoom_func)
		app.SetCameraMaxDistance(100000)

	def MobberSlotFunc(self):
		global Mobber_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			item.SelectItem(attachedSlotVnum)

			Mobber_ID = mouseModule.mouseController.GetAttachedItemIndex()
			mouseModule.mouseController.DeattachObject()

			item.SelectItem(int(attachedSlotVnum))
			self.MobberSlotIcon.LoadImage(str(item.GetIconImageFileName()))

	def Set_Poty_1_ID(self):
		global Poty_1_ID
		global Poty_1_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()

			Poty_1_ID = mouseModule.mouseController.GetAttachedItemIndex()
			item.SelectItem(attachedSlotVnum)

		item.SelectItem(int(attachedSlotVnum))
		self.PotySlotIcon.LoadImage(str(item.GetIconImageFileName()))
		mouseModule.mouseController.DeattachObject()


	def Set_Poty_2_ID(self):
		global Poty_2_ID
		global Poty_2_Icon
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()

			Poty_2_ID = mouseModule.mouseController.GetAttachedItemIndex()
			item.SelectItem(attachedSlotVnum)

		item.SelectItem(int(attachedSlotVnum))
		self.PotySlotIcon2.LoadImage(str(item.GetIconImageFileName()))
		mouseModule.mouseController.DeattachObject()




	def SetItemSlot(self, renderingSlotNumber, ItemIndex, ItemCount = 0):
		if 0 == ItemIndex or None == ItemIndex:
			wndMgr.ClearSlot(self.hWnd, renderingSlotNumber)
			return

		item.SelectItem(ItemIndex)
		itemIcon = item.GetIconImage()

		item.SelectItem(ItemIndex)
		(width, height) = item.GetItemSize()

		wndMgr.SetSlot(self.hWnd, renderingSlotNumber, ItemIndex, width, height, itemIcon)
		wndMgr.SetSlotCount(self.hWnd, renderingSlotNumber, ItemCount)

	def SelectEmptySlot(self, slot):
		global Dopalacz_ID,Slotlista,cfg,xox,Dopalacz_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			itemVnum = player.GetItemIndex(attachedSlotPos)
			Dopalacz_ID[xox] = (attachedSlotVnum)
			Slotlista[xox] = (slot)
			self.itemlist[slot] = attachedSlotPos
			xox += 1
			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				self.gives.SetItemSlot(slot, itemVnum)
		mouseModule.mouseController.DeattachObject()

	def SelectEmptySlot1(self, slot):
		global xoxx,Otwieracz_ID
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			itemVnum = player.GetItemIndex(attachedSlotPos)
			Otwieracz_ID[xoxx] = (attachedSlotVnum)
			self.itemlist1[slot] = attachedSlotPos
			xoxx += 1
			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				self.gives1.SetItemSlot(slot, itemVnum)
		mouseModule.mouseController.DeattachObject()


	def Dzien_func(self):
		background.SetEnvironmentData(0)

	def Noc_func(self):
		background.SetEnvironmentData(1)

	def Gora_func(self):
		myVid = player.GetMainCharacterIndex()
		chr.SelectInstance(myVid)
		(x, y, z) = player.GetMainCharacterPosition()
		chr.SetPixelPosition(int(x), int(y) - 2000, int(z))
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)


	def Lewo_func(self):
		myVid = player.GetMainCharacterIndex()
		chr.SelectInstance(myVid)
		(x, y, z) = player.GetMainCharacterPosition()
		chr.SetPixelPosition(int(x) - 2000, int(y), int(z))
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

	def Prawo_func(self):
		myVid = player.GetMainCharacterIndex()
		chr.SelectInstance(myVid)
		(x, y, z) = player.GetMainCharacterPosition()
		chr.SetPixelPosition(int(x) + 2000, int(y), int(z))
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

	def Dol_func(self):
		myVid = player.GetMainCharacterIndex()
		chr.SelectInstance(myVid)
		(x, y, z) = player.GetMainCharacterPosition()
		chr.SetPixelPosition(int(x), int(y) + 2000, int(z))
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

	def Tpdokordow_func(self):
		Position_X = self.Xin.GetText()
		Position_Y = self.Yin.GetText()
		Position_X = int(Position_X)
		Position_Y = int(Position_Y)

		global TeleportState, Debug, GetCurrentMapSize, TeleportToDest, DivideToFloat
		myVid = player.GetMainCharacterIndex()
		chr.SelectInstance(myVid)
		self.TeleportToDest((Position_X+10)*100,(Position_Y+10)*100)
		chr.MoveToDestPosition(int(myVid),Position_X*100,Position_Y*100)
		net.DirectEnter(3)
	def Zamknijgre_func(self):
		app.Exit()

	def AutoAtak_func(self, arg):
		if arg=='on':
			self.AutoAttackStartFunc()
			self.AutoAtak.SetText(Przyciskon+'Auto Atak')
		elif arg=='off':
			self.AutoAttackStopFunc()
			self.AutoAtak.SetText(Przyciskoff+'Auto Atak')
	def AutoAttackStartFunc(self):
		self.AutoAttackx = XX()
		self.AutoAttackx.XX1(5)
		self.AutoAttackx.XX2(self.AutoAttackStartFunc)
		if self.Autoaacombo.GetCurrentText() == 'Normal':
			player.SetAttackKeyState(TRUE)

		if self.Autoaacombo.GetCurrentText() == 'Rotacyjny':
			Direction = app.GetRandom(0,7)
			player.SetAttackKeyState(TRUE)
			chr.SetDirection(Direction)
	def AutoAttackStopFunc(self):
		player.SetAttackKeyState(FALSE)
		self.AutoAttackx=XX()
		self.AutoAttackx.XX1(999999999999)
		self.AutoAttackx.XX2(self.AutoAttackStopFunc)
		player.SetAttackKeyState(FALSE)

	def Poty_func(self, arg):
		if arg=='on':
			self.PotyStartFunc()
			self.Poty.SetText(Przyciskon+'Auto Poty')
		elif arg=='off':
			self.PotyStopFunc()
			self.Poty.SetText(Przyciskoff+'Auto Poty')


	def PotyStartFunc(self):
		global Poty
		global Poty_1_ID
		global Poty_2_ID

		Potyt = self.Potyhpczas.GetText()
		maxhp = player.GetStatus(player.MAX_HP)
		aktualnehp = player.GetStatus(player.HP)
		if (float(aktualnehp) / float(maxhp)) * 100 < int(int(Potyt)):
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				CzerwonePotki = player.GetItemIndex(i)
				if CzerwonePotki == (int(Poty_1_ID)):
					net.SendItemUsePacket(i)
					break

		Potyt1 = self.Potympczas.GetText()
		maxmp = player.GetStatus(player.MAX_SP)
		aktualnemp = player.GetStatus(player.SP)
		if (float(aktualnemp) / float(maxmp)) * 100 < int(int(Potyt1)):
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				NiebieskiePotki = player.GetItemIndex(i)
				if NiebieskiePotki == (int(Poty_2_ID)):
					net.SendItemUsePacket(i)
					break


		self.Potyx = XX()
		self.Potyx.XX1(float(0.1))
		self.Potyx.XX2(self.PotyStartFunc)


	def PotyStopFunc(self):
		self.Potyx = XX()
		self.Potyx.XX1(float(99999999999999999))
		self.Potyx.XX2(self.PotyStopFunc)

	def Mobber_func(self, arg):
		if arg=='on':
			self.MobberStartFunc()
			self.Mobberek.SetText(Przyciskon+'Mobber')
		elif arg=='off':
			self.MobberStopFunc()
			self.Mobberek.SetText(Przyciskoff+'Mobber')

	def MobberStartFunc(self):
		global Mobber_ID,cipa
		if self.Mobbercombo.GetCurrentText() == 'Normal':
			mobbert = self.Peleczas.GetText()
			self.Mobber=XX()
			self.Mobber.XX1(int(mobbert))
			self.Mobber.XX2(self.MobberStartFunc)
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Mobberitemx = player.GetItemIndex(i)
				if Mobberitemx == (int(Mobber_ID)):
					net.SendItemUsePacket(i)
					break

		if self.Mobbercombo.GetCurrentText() == 'Mega':
			self.Mobber=XX()
			self.Mobber.XX1(float(0.2))
			self.Mobber.XX2(self.MobberStartFunc)
			myVid = player.GetMainCharacterIndex()
			mobbert = self.Peleczas.GetText()
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				Mobberitemx = player.GetItemIndex(i)
				if Mobberitemx == (int(Mobber_ID)):
					net.SendItemUsePacket(i)
					break
					i=i
			a=1
			while a:
				x, y, z = player.GetMainCharacterPosition()
				if cipa == 0:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x) - 1200, int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 1:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x) - 1200, int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 2:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x) + 1200, int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 3:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x) + 1200, int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 4:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x), int(y) - 1200, int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 5:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x), int(y) - 1200, int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 6:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x), int(y) + 1200, int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 7:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x), int(y) + 1200, int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 8:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x) + 1200, int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 9:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x) + 1200, int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 10:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x) - 1200, int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 11:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x) - 1200, int(y), int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 12:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x), int(y) + 1200, int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 13:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x), int(y) + 1200, int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 14:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x), int(y) - 1200, int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = cipa + 1
					continue
				if cipa == 15:
					chr.SelectInstance(myVid)
					chr.SetPixelPosition(int(x), int(y) - 1200, int(z))
					player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
					player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
					net.SendItemUsePacket(i)
					net.SendItemUsePacket(i)
					a = 0
					cipa = 0
					self.Mobber=XX()
					self.Mobber.XX1(int(mobbert))
					self.Mobber.XX2(self.MobberStartFunc)
					continue
	def MobberStopFunc(self):
		self.Mobber=XX()
		self.Mobber.XX1(100000000)
		self.Mobber.XX2(self.MobberStopFunc)
		a = 0
		cipa = 0


	def Dopalacze_func(self, arg):
		if arg=='on':
			self.DopalaczStartFunc()
			self.Dopalacze.SetText(Przyciskon+'Dopalacze')
		elif arg=='off':
			self.DopalaczStopFunc()
			self.Dopalacze.SetText(Przyciskoff+'Dopalacze')

	def DopalaczStartFunc(self):
		global Dopalaczx
		global Dopalacz_ID
		global Otwieraczt


		for i in xrange(player.INVENTORY_PAGE_SIZE*5):
			for x in xrange(0,28):
				if player.GetItemIndex(i) == int(Dopalacz_ID[x]):
					net.SendItemUsePacket(i)
					break


		Otwieraczt = self.Coiledopyin.GetText()
		Otwieraczt = int(Otwieraczt)*60
		self.Delay_Dopalacz = XX()
		self.Delay_Dopalacz.XX1(float(Otwieraczt))
		self.Delay_Dopalacz.XX2(self.DopalaczStartFunc)

	def DopalaczStopFunc(self):
		self.Delay_Dopalacz = XX()
		self.Delay_Dopalacz.XX1(float(99999999999999999))
		self.Delay_Dopalacz.XX2(self.DopalaczStopFunc)

	def Ghost_func(self):
		chr.Revive()

	def Kamera_func(self, arg):
		if arg=='on':
			x, y, z = player.GetMainCharacterPosition()
			app.SetCameraSetting(int(x), int(-y), int(z), 5000, 10, 30)
			self.Kamera.SetText(Przyciskon+'Zatrzymaj kamere')
		elif arg=='off':
			app.SetDefaultCamera()
			self.Kamera.SetText(Przyciskoff+'Zatrzymaj kamere')

	def Snieg_func(self, arg):
		if arg=='on':
			background.EnableSnow(1)
			self.Snieg.SetText(Przyciskon+'Snieg')
		elif arg=='off':
			background.EnableSnow(0)
			self.Snieg.SetText(Przyciskoff+'Snieg')

	def Combo_func(self, arg):
		if arg=='on':
			chr.testSetComboType(2)
			self.Combo.SetText(Przyciskon+'Combo')

		elif arg=='off':
			chr.testSetComboType(0)
			self.Combo.SetText(Przyciskoff+'Combo')

	def Otwieracz_func(self, arg):
		if arg=='on':
			self.OtwieraczStartFunc()
			self.Otwieraj.SetText(Przyciskon+'Otwieraj')
		elif arg=='off':
			self.OtwieraczStopFunc()
			self.Otwieraj.SetText(Przyciskoff+'Otwieraj')

	def OtwieraczStartFunc(self):
		global Otwieraczx
		global Otwieracz_ID

		for x in xrange(0,9):
			for i in xrange(player.INVENTORY_PAGE_SIZE*5):
				if player.GetItemIndex(i) == int(Otwieracz_ID[x]):
					net.SendItemUsePacket(i)
					break

		Otwieraczt1 = self.Dopyczas.GetText()
		self.Delay_Otwieracz = XX()
		self.Delay_Otwieracz.XX1(float(Otwieraczt1))
		self.Delay_Otwieracz.XX2(self.OtwieraczStartFunc)



	def OtwieraczStopFunc(self):
		self.Delay_Otwieracz = XX()
		self.Delay_Otwieracz.XX1(float(99999999999999999))
		self.Delay_Otwieracz.XX2(self.OtwieraczStopFunc)

	def AutoWstawanie_func(self, arg):
		if arg=='on':
			self.Autowstawaniestart()
			self.AutoWstawanie.SetText(Przyciskon+'Auto Wstawanie')
		elif arg=='off':
			self.Autowstawaniestop()
			self.AutoWstawanie.SetText(Przyciskoff+'Auto Wstawanie')

	def Autowstawaniestart(self):
		global autowtawanie_pozwo
		self.awfunc=XX()
		self.awfunc.XX1(15.0)
		self.awfunc.XX2(self.Autowstawaniestart)
		maxhp=player.GetStatus(player.MAX_HP)
		aktualnehp=player.GetStatus(player.HP)
		if autowtawanie_pozwo == 1 and float(aktualnehp) / float(maxhp) * 100 >= int(50):
			#oldSendChatPacket('Start')
			autowtawanie_pozwo = 0
		if float(aktualnehp) / float(maxhp) * 100 <= int(0):
			player.SetAttackKeyState(FALSE)
			#oldSendChatPacket('Stop')
			oldSendChatPacket('/restart_here')
			autowtawanie_pozwo = 1

	def Autowstawaniestop(self):
		self.awfunc=XX()
		self.awfunc.XX1(100000000.0)
		self.awfunc.XX2(self.Autowstawaniestop)

	def Crashmap_func(self, arg):
		if arg=='on':
			self.Crashmapstart()
			self.CrashMap.SetText(Przyciskon+'Crash map')
		elif arg=='off':
			self.Crashmapstop()
			self.CrashMap.SetText(Przyciskoff+'Crash map')

	def Crashmapstart(self):
		Current_Map_Name = background.GetCurrentMapName()
		x,y = player.GetMainCharacterPosition()[:2]
		background.LoadMap(str(Current_Map_Name), x, y, 0)

	def Crashmapstop(self):
		Current_Map_Name = background.GetCurrentMapName()
		background.LoadMap(str(Current_Map_Name), 100, 100, 0)
		self.Crashmap=XX()
		self.Crashmap.XX1(9999999999999999999999.0)
		self.Crashmap.XX2(self.Crashmapstart)

	def WykrywaczGM_func(self, arg):
		global Szukanie_gm,wykrywaczzero
		if wykrywaczzero == 0:
			self.WykrywaczFuncStart()
			wykrywaczzero = 1
		if arg=='on':
			Szukanie_gm = 1
			self.WykrywaczGM.SetText(Przyciskon+'Wykrywacz GM')
		elif arg=='off':
			Szukanie_gm = 0
			self.WykrywaczGM.SetText(Przyciskoff+'Wykrywacz GM')

	def SzukajMetinow_func(self, arg):
		global Szukanie_metinow, wykrywaczzero
		if wykrywaczzero == 0:
			self.WykrywaczFuncStart()
			wykrywaczzero = 1
		if arg=='on':
			Szukanie_metinow = 1
			self.SzukajMetinow.SetText(Przyciskon+'Szukaj')
		elif arg=='off':
			Szukanie_metinow = 0
			self.SzukajMetinow.SetText(Przyciskoff+'Szukaj')
			self.Nazwametina2x.SetText('')
			self.Pozycjametinax2x.SetText('')
			self.Pozycjametinay2x.SetText('')

	def WykrywaczFuncStart(self):
		global ks,Position_Metin_X,Position_Metin_Y,bosy,Position_Boss_Y,Position_Boss_X,Szukanie_metinow,Szukanie_bosow,Szukanie_gm,TargetVid2,TargetVid,VidyPozwolenie,ListaVidow,ListaVidow2,listash2
		self.Wykrywaczmetinow=XX()
		self.Wykrywaczmetinow.XX1(1)
		self.Wykrywaczmetinow.XX2(self.WykrywaczFuncStart)
		if Szukanie_bosow == 1 or Szukanie_gm == 1 or Szukanie_metinow == 1:


			for i in listash2:
				Odleglosc = player.GetCharacterDistance(i)
				Typ = chr.GetInstanceType(i)
				if Typ==6 and Szukanie_gm == 1:
					Nazwa=chr.GetNameByVID(i)
					if Nazwa[0] == '[':
						Pozycja = player.GetMainCharacterPosition(i)
						Nazwa=chr.GetNameByVID(i)
						(x,y,z)= chr.GetPixelPosition(i)
						if self.GmCombo.GetCurrentText() == 'Informacja':
								dbg.LogBox(str(Nazwa) + '  x:'+(str(x/100) + '  y:'+(str(y/100))))
						if self.GmCombo.GetCurrentText() == 'Wyloguj':
								net.DirectEnter(9)
						if self.GmCombo.GetCurrentText() == 'Wyjdz z gry':
								app.Exit()
				if Typ==2 and Szukanie_metinow == 1:
					player.SetTarget(i)
					if player.GetTargetVID() != 0:
						MojVidzik =  player.GetTargetVID()
					imie=chr.GetNameByVID(i)
					chr.SelectInstance(i)
					(X, Y, Z) = chr.GetPixelPosition(i)
					Position_Metin_X = X
					Position_Metin_Y = Y
					X = X / 100
					Y = Y / 100
					X = str(round(X))
					Y = str(round(Y))
					X = X.replace('.0', '')
					Y = Y.replace('.0', '')
					yt = player.GetMainCharacterPosition()
					self.NazwametinaBok.SetText('Nazwa Metina:' + Przyciskon + imie)
					self.BoardMetin.Show()
					self.Nazwametina2x.SetText(imie)
					self.Pozycjametinax2x.SetText(X)
					self.Pozycjametinay2x.SetText(Y)
				if Typ==0 and Szukanie_bosow == 1:
					player.SetTarget(i)
					if player.GetTargetVID() != 0:
						MojVidzik =  player.GetTargetVID()
					chr.SelectInstance(i)
					Race=chr.GetRace(i)
					for k in bosy:
						if Race==int(k):
							imie=chr.GetNameByVID(i)
							chr.SelectInstance(i)
							(X, Y, Z) = chr.GetPixelPosition(i)
							Position_Boss_X = X
							Position_Boss_Y = Y
							X = X / 100
							Y = Y / 100
							X = str(round(X))
							Y = str(round(Y))
							X = X.replace('.0', '')
							Y = Y.replace('.0', '')
							self.Nazwabossa2x.SetText(imie)
							self.Pozycjabossax2x.SetText(X)
							self.Pozycjabossay2x.SetText(Y)
							self.NazwabossaBok.SetText('Nazwa Bossa:' + Przyciskon + imie)
							self.BoardBoss.Show()


	def WykrywaczFuncStop(self):
		global ks
		self.Wykrywaczmetinow=XX()
		self.Wykrywaczmetinow.XX1(100000000.0)
		self.Wykrywaczmetinow.XX2(self.WykrywaczMetinowFuncStop)


	def Krzycz1(self):
		global bosy
		if os.path.exists('c:montes_cfg/Bossy.cfg'):
			kordziki = open('c:montes_cfg/Bossy.cfg', 'r').read().split()
			for x in xrange(len(kordziki)):
				lol = self.BossyInfo.GetText()
				self.BossyInfo.SetText(str(lol+' '+kordziki[x]))
				bosy.append(kordziki[x])

	def ZapiszBossy(self):
		try:
			os.mkdir('C:montes_cfg')
		except:
			pass
		save = open('c:montes_cfg/Bossy.cfg', 'w')
		lol = self.BossyInfo.GetText()
		save.write(str(lol))
		save.close()

	def DodajBossa_func(self):
		vid = player.GetTargetVID()
		if vid != -1 or vid != 0:
			chr.SelectInstance(vid)
			race=chr.GetRace(vid)
			bosy.append(int(race))
		lol = self.BossyInfo.GetText()
		self.BossyInfo.SetText(str(lol)+ ' ' + str(race))
		self.ZapiszBossy()


	def SzukajBossow_func(self, arg):
		global Szukanie_bosow
		if arg=='on':
			Szukanie_bosow = 1
			self.SzukajBossow.SetText(Przyciskon+'Szukaj')
		elif arg=='off':
			Szukanie_bosow = 0
			self.SzukajBossow.SetText(Przyciskoff+'Szukaj')
			self.Nazwabossa2x.SetText('')
			self.Pozycjabossax2x.SetText('')
			self.Pozycjabossay2x.SetText('')

	def WykrywaczMetinowFuncStartx(self):
		global Position_Metin_Y,Position_Metin_X
		Position_Metin_X1 = int(Position_Metin_X)
		Position_Metin_Y1 = int(Position_Metin_Y)

		global TeleportState, Debug, GetCurrentMapSize, TeleportToDest, DivideToFloat
		myVid = player.GetMainCharacterIndex()
		chr.SelectInstance(myVid)
		self.TeleportToDest(Position_Metin_X1,Position_Metin_Y1)

	def WykrywaczBossowFuncStartx(self):
		global Position_Boss_Y,Position_Boss_X
		Position_Boss_X1 = int(Position_Boss_X)
		Position_Boss_Y1 = int(Position_Boss_Y)

		global TeleportState, Debug, GetCurrentMapSize, TeleportToDest, DivideToFloat
		myVid = player.GetMainCharacterIndex()
		chr.SelectInstance(myVid)
		self.TeleportToDest(Position_Boss_X1,Position_Boss_Y1)
	def usunpotehp(self):
		global Poty_1_ID
		Poty_1_ID = 0
		self.PotySlotIcon.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')

	def usunpotemp(self):
		global Poty_2_ID
		Poty_2_ID = 0
		self.PotySlotIcon2.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')

	def usunpele(self):
		global Mobber_ID
		Mobber_ID = 0
		self.MobberSlotIcon.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')

	def usundopy(self):
		global Dopalacz_ID,Slotlista,xox
		xox = 0
		for x in xrange(999):
			self.gives.ClearSlot(x)
			self.gives.RefreshSlot()

		Dopalacz_ID = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		Slotlista = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	def usunotw(self):
		global xoxx,Otwieracz_ID
		xoxx = 0
		for x in xrange(999):
			self.gives1.ClearSlot(x)
			self.gives1.RefreshSlot()

		Otwieracz_ID = [0,0,0,0,0,0,0,0,0]

	def Ulepsz_func(self):
		global SlotUlepszania,SlotUlepszaniaDO
		a = int(self.Oileulepszycin.GetText())
		for i in xrange(int(a)):
			if self.UlepszanieCombo.GetCurrentText() == 'Kowal':
				net.SendRefinePacket(SlotUlepszania, 0)

			if self.UlepszanieCombo.GetCurrentText() == 'Kowal Gildyjny':
				net.SendRefinePacket(SlotUlepszania, 1)

			if self.UlepszanieCombo.GetCurrentText() == 'Zwoj Blogoslawienstwa':
				for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*5):
					ItemValue = player.GetItemIndex(InventorySlot)
					if ItemValue == 25040:
						net.SendItemUseToItemPacket(InventorySlot, SlotUlepszania)
						net.SendRefinePacket(SlotUlepszania, 2)
						break

			if self.UlepszanieCombo.GetCurrentText() == 'Magiczny Metal':
				for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*5):
					ItemValue = player.GetItemIndex(InventorySlot)
					if ItemValue == 25041:
						net.SendItemUseToItemPacket(InventorySlot, SlotUlepszania)
						net.SendRefinePacket(SlotUlepszania, 3)
						break

			if self.UlepszanieCombo.GetCurrentText() == 'Inne':
				for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*5):
					ItemValue = player.GetItemIndex(InventorySlot)
					if ItemValue == SlotUlepszaniaDO:
						net.SendItemUseToItemPacket(InventorySlot, SlotUlepszania)
						net.SendRefinePacket(SlotUlepszania, 2)
						break

			if self.UlepszanieCombo.GetCurrentText() == 'DT':
				net.SendRefinePacket(SlotUlepszania, 4)



	def Spamboton(self):
		if self.Spambotp.GetCurrentText() == '|cff00FF00|H|hZielony':
			oldSendChatPacket('|cff00FF00|H|h' + self.Tekstin.GetText())
		if self.Spambotp.GetCurrentText() == '|cFFFF0000|Hitem|hCzerwony':
			oldSendChatPacket('|cFFFF0000|Hitem|h' + self.Tekstin.GetText())
		if self.Spambotp.GetCurrentText() == '|cffFFFFFF|H|hNormal':
			oldSendChatPacket(self.Tekstin.GetText())
		if self.Spambotp.GetCurrentText() == '|cffFFFF00|H|hZolty':
			oldSendChatPacket('|cffFFFF00|H|h' + self.Tekstin.GetText())
		if self.Spambotp.GetCurrentText() == '|cFFFF00FF|Hitem|hRozowy':
			oldSendChatPacket('|cFFFF00FF|Hitem|h' + self.Tekstin.GetText())
		if self.Spambotp.GetCurrentText() == '|cFF804000|Hitem|hBrazowy':
			oldSendChatPacket('|cFF804000|Hitem|h' + self.Tekstin.GetText())
		if self.Spambotp.GetCurrentText() == '|cffffc700|Hitem|hZloty':
			oldSendChatPacket('|cffffc700|Hitem|h' + self.Tekstin.GetText())
		if self.Spambotp.GetCurrentText() == '|cff800080|H|hFiolotowy':
			oldSendChatPacket('|cff800080|H|h' + self.Tekstin.GetText())
		if self.Spambotp.GetCurrentText() == '|cFF0080FF|Hitem|hNiebieski':
			oldSendChatPacket('|cFF0080FF|Hitem|h' + self.Tekstin.GetText())
		if self.Spambotp.GetCurrentText() == '|cff00FFFF|H|hBlekitny':
			oldSendChatPacket('|cff00FFFF|H|h' + self.Tekstin.GetText())

		self.Spambotk=XX()
		self.Spambotk.XX1(float(self.Coilespamtxtin.GetText()))
		self.Spambotk.XX2(self.Spamboton)

	def Spambotoff(self):
		self.Spambotk=XX()
		self.Spambotk.XX1(float(9999999999999))
		self.Spambotk.XX2(self.Spambotoff)

	def Spamboton1(self):
		if self.Spambotp.GetCurrentText() == '|cff00FF00|H|hZielony':
			oldSendChatPacket('|cff00FF00|H|h' + self.Tekstin.GetText(),chat.CHAT_TYPE_SHOUT)
		if self.Spambotp.GetCurrentText() == '|cFFFF0000|Hitem|hCzerwony':
			oldSendChatPacket('|cFFFF0000|Hitem|h' + self.Tekstin.GetText(),chat.CHAT_TYPE_SHOUT)
		if self.Spambotp.GetCurrentText() == '|cffFFFFFF|H|hNormal':
			oldSendChatPacket(self.Tekstin.GetText(),chat.CHAT_TYPE_SHOUT)
		if self.Spambotp.GetCurrentText() == '|cffFFFF00|H|hZolty':
			oldSendChatPacket('|cffFFFF00|H|h' + self.Tekstin.GetText(),chat.CHAT_TYPE_SHOUT)
		if self.Spambotp.GetCurrentText() == '|cFFFF00FF|Hitem|hRozowy':
			oldSendChatPacket('|cFFFF00FF|Hitem|h' + self.Tekstin.GetText(),chat.CHAT_TYPE_SHOUT)
		if self.Spambotp.GetCurrentText() == '|cFF804000|Hitem|hBrazowy':
			oldSendChatPacket('|cFF804000|Hitem|h' + self.Tekstin.GetText(),chat.CHAT_TYPE_SHOUT)
		if self.Spambotp.GetCurrentText() == '|cffffc700|Hitem|hZloty':
			oldSendChatPacket('|cffffc700|Hitem|h' + self.Tekstin.GetText(),chat.CHAT_TYPE_SHOUT)
		if self.Spambotp.GetCurrentText() == '|cff800080|H|hFiolotowy':
			oldSendChatPacket('|cff800080|H|h' + self.Tekstin.GetText(),chat.CHAT_TYPE_SHOUT)
		if self.Spambotp.GetCurrentText() == '|cFF0080FF|Hitem|hNiebieski':
			oldSendChatPacket('|cFF0080FF|Hitem|h' + self.Tekstin.GetText(),chat.CHAT_TYPE_SHOUT)
		if self.Spambotp.GetCurrentText() == '|cff00FFFF|H|hBlekitny':
			oldSendChatPacket('|cff00FFFF|H|h' + self.Tekstin.GetText(),chat.CHAT_TYPE_SHOUT)



		self.Spambotk=XX()
		self.Spambotk.XX1(float(self.Coilespamtxtin.GetText()))
		self.Spambotk.XX2(self.Spamboton1)

	def Spambotoff1(self):
		self.Spambotk=XX()
		self.Spambotk.XX1(float(9999999999999))
		self.Spambotk.XX2(self.Spambotoff1)


	def Spambtn_func(self, arg):
		if arg=='on':
			self.Spamboton()
			self.Spambtn.SetText(Przyciskon + 'Normal')
		elif arg=='off':
			self.Spambotoff()
			self.Spambtn.SetText(Przyciskoff + 'Normal')

	def Spambtn_func1(self, arg):
		if arg=='on':
			self.Spamboton1()
			self.Spambtn1.SetText(Przyciskon + 'Wolaj')
		elif arg=='off':
			self.Spambotoff1()
			self.Spambtn1.SetText(Przyciskoff + 'Wolaj')


	def Skill3Buff_func(self, arg):
		if arg=='on':
			self.Skill3Buff()
		elif arg=='off':
			self.Skill3Buffstop()

	def Skill4Buff_func(self, arg):
		if arg=='on':
			self.Skill4Buff()
		elif arg=='off':
			self.Skill4Buffstop()

	def Skill5buff_func(self, arg):
		if arg=='on':
			self.Skill5buff()
		elif arg=='off':
			self.Skill5buffstop()

	def Skill6buff_func(self, arg):
		if arg=='on':
			self.Skill6buff()
		elif arg=='off':
			self.Skill6buffstop()

	def Skill6buff_func1(self, arg):
		if arg=='on':
			self.Skill6buff1()
		elif arg=='off':
			self.Skill6buffstop1()

	def horse(self):
		oldSendChatPacket('/ride')

	def Skil3(self):
		player.ClickSkillSlot(3)

	def Skil4(self):
		player.ClickSkillSlot(4)

	def Skil5(self):
		player.ClickSkillSlot(5)

	def Skil6(self):
		player.ClickSkillSlot(6)

	def Skill3Buff(self):
		if player.IsMountingHorse():
			oldSendChatPacket('/unmount')
			self.Skill30 = XX()
			self.Skill30.XX1(1)
			self.Skill30.XX2(self.Skil3)
			self.Skill31 = XX()
			self.Skill31.XX1(1.5)
			self.Skill31.XX2(self.horse)
			self.Skill32 = XX()
			self.Skill32.XX1(int(self.Skill2czas.GetText()))
			self.Skill32.XX2(self.Skill3Buff)
		else:
			self.Skill30 = XX()
			self.Skill30.XX1(1)
			self.Skill30.XX2(self.Skil3)
			self.Skill32 = XX()
			self.Skill32.XX1(int(self.Skill2czas.GetText()))
			self.Skill32.XX2(self.Skill3Buff)

	def Skill3Buffstop(self):
		self.Skill32 = XX()
		self.Skill32.XX1(int(9999999999999))
		self.Skill32.XX2(self.Skill3Buff)

	def Skill4Buff(self):
		if player.IsMountingHorse():
			oldSendChatPacket('/unmount')
			self.Skill40 = XX()
			self.Skill40.XX1(1)
			self.Skill40.XX2(self.Skil4)
			self.Skill41 = XX()
			self.Skill41.XX1(1.5)
			self.Skill41.XX2(self.horse)
			self.Skill42 = XX()
			self.Skill42.XX1(int(self.Skill1czas.GetText()))
			self.Skill42.XX2(self.Skill4Buff)
		else:
			self.Skill40 = XX()
			self.Skill40.XX1(1)
			self.Skill40.XX2(self.Skil4)
			self.Skill42 = XX()
			self.Skill42.XX1(int(self.Skill1czas.GetText()))
			self.Skill42.XX2(self.Skill4Buff)
	def Skill4Buffstop(self):
		self.Skill42 = XX()
		self.Skill42.XX1(int(9999999999999))
		self.Skill42.XX2(self.Skill4Buff)

	def Skill5buff(self):
		if player.IsMountingHorse():
			oldSendChatPacket('/unmount')
			self.Skill50 = XX()
			self.Skill50.XX1(1)
			self.Skill50.XX2(self.Skil5)
			self.Skill51 = XX()
			self.Skill51.XX1(1.5)
			self.Skill51.XX2(self.horse)
			self.Skill52 = XX()
			self.Skill52.XX1(int(self.Skill3czas.GetText()))
			self.Skill52.XX2(self.Skill5buff)
		else:
			self.Skill50 = XX()
			self.Skill50.XX1(1)
			self.Skill50.XX2(self.Skil5)
			self.Skill52 = XX()
			self.Skill52.XX1(int(self.Skill3czas.GetText()))
			self.Skill52.XX2(self.Skill5buff)
	def Skill5buffstop(self):
		self.Skill52 = XX()
		self.Skill52.XX1(int(9999999999))
		self.Skill52.XX2(self.Skill5buff)

	def Skill6buff(self):
		if player.IsMountingHorse():
			oldSendChatPacket('/unmount')
			self.Skill60 = XX()
			self.Skill60.XX1(1)
			self.Skill60.XX2(self.Skil6)
			self.Skill61 = XX()
			self.Skill61.XX1(1.5)
			self.Skill61.XX2(self.horse)
			self.Skill62 = XX()
			self.Skill62.XX1(int(self.Skill1czas.GetText()))
			self.Skill62.XX2(self.Skill6buff)
		else:
			self.Skill60 = XX()
			self.Skill60.XX1(1)
			self.Skill60.XX2(self.Skil6)
			self.Skill62 = XX()
			self.Skill62.XX1(int(self.Skill1czas.GetText()))
			self.Skill62.XX2(self.Skill6buff)

	def Skill6buffstop(self):
		self.Skill62 = XX()
		self.Skill62.XX1(int(999999999))
		self.Skill62.XX2(self.Skill6buff)

	def Skill6buff1(self):
		if player.IsMountingHorse():
			oldSendChatPacket('/unmount')
			self.Skill601 = XX()
			self.Skill601.XX1(1)
			self.Skill601.XX2(self.Skil6)
			self.Skill611 = XX()
			self.Skill611.XX1(1.5)
			self.Skill611.XX2(self.horse)
			self.Skill621 = XX()
			self.Skill621.XX1(int(self.Skill2czas.GetText()))
			self.Skill621.XX2(self.Skill6buff1)
		else:
			self.Skill60 = XX()
			self.Skill60.XX1(1)
			self.Skill60.XX2(self.Skil6)
			self.Skill62 = XX()
			self.Skill62.XX1(int(self.Skill1czas.GetText()))
			self.Skill62.XX2(self.Skill6buff)
	def Skill6buffstop1(self):
		self.Skill621 = XX()
		self.Skill621.XX1(int(999999999))
		self.Skill621.XX2(self.Skill6buff1)

	def DodajItem_func(self):
		self.opcje()

	def UsunItem_func(self):
		self.delall()



	def pickupn_func(self, arg):
		if arg=='on':
			self.PickUpStartFunc()
			self.pickupn.SetText(Przyciskon+'Normal Pickup')
		elif arg=='off':
			self.PickUpStopFunc()
			self.pickupn.SetText(Przyciskoff+'Normal Pickup')

	def PickUpStartFunc(self):
		self.PickUp=XX()
		self.PickUp.XX1(0.001)
		self.PickUp.XX2(self.PickUpStartFunc)
		player.PickCloseItem()

	def PickUpStopFunc(self):
		self.PickUp=XX()
		self.PickUp.XX1(100000000)
		self.PickUp.XX2(self.PickUpStopFunc)


	def pickall_func(self, arg):
		if arg=='on':
			self.Pickupallon()
			self.pickall.SetText(Przyciskon+'Pick Wszystko')
		elif arg=='off':
			self.Pickupalloff()
			self.pickall.SetText(Przyciskoff+'Pick Wszystko')

	def pickwyb_func(self, arg):
		if arg=='on':
			self.Pickupwybraneon()
			self.pickwyb.SetText(Przyciskon+'Pick Wybrane')
		elif arg=='off':
			self.Pickupwybraneoff()
			self.pickwyb.SetText(Przyciskoff+'Pick Wybrane')

	def Pickupwybraneon(self):
		global List,dupa,ciul
		self.PickupwybraneonXX=XX()
		self.PickupwybraneonXX.XX1(1)
		self.PickupwybraneonXX.XX2(self.Pickupwybraneon)
		Picker=textTail.Pick
		for y in xrange(125,600,9):
			for x in xrange(300,825,31):
				iVID = Picker(x, y)
				if iVID != -1 and iVID not in List:
					for i in xrange(35):
						if iVID!=Picker(x-i,y):
							if Picker(x-i+1,y)==iVID:
								poczatek=x-i
					for i in xrange(500):
						if iVID!=Picker(x+i,y):
							if iVID==Picker(x+i-1,y):
								koniec=x+i
								f=koniec-poczatek+1
								for a in self.ciul:
									if f==a:
										dupa.append(iVID)
					List.append(iVID)

		if len(List)!=0:
			for i in dupa:
				net.SendItemPickUpPacket(i)

	def Pickupwybraneoff(self):
		self.PickupwybraneonXX=XX()
		self.PickupwybraneonXX.XX1(999999999.0)
		self.PickupwybraneonXX.XX2(self.Pickupwybraneon)

	def Pickupallon(self):
		self.PickupallonXX=XX()
		self.PickupallonXX.XX1(1.0)
		self.PickupallonXX.XX2(self.Pickupallon)
		List=[]
		Picker=textTail.Pick
		for y in xrange(125,600,9):
			for x in xrange(300,825,31):
				iVID = Picker(x, y)
				if iVID != -1 and iVID not in List:
					List.append(iVID)
		if len(List)!=0:
			for i in List:
				net.SendItemPickUpPacket(i)


	def Pickupalloff(self):
		self.PickupallonXX=XX()
		self.PickupallonXX.XX1(100000000.0)
		self.PickupallonXX.XX2(self.Pickupallon)

	def opcje(self):
		List=[]
		Picker=textTail.Pick
		for y in xrange(125,1600,9):
			for x in xrange(300,1825,31):
				iVID = Picker(x, y)
				if iVID != -1 and iVID not in List:
					for i in xrange(35):
						if iVID!=Picker(x-i,y):
							if Picker(x-i+1,y)==iVID:
								poczatek=x-i
					for i in xrange(500):
						if iVID!=Picker(x+i,y):
							koniec=x+i
							self.ciul.append(koniec-poczatek+1)
							f=str(koniec-poczatek+1)
							self.list_Pickupselect.AppendItem(Item(f))
							break

					List.append(iVID)


	def delall(self):
		self.list_Pickupselect.RemoveAllItems()
		self.ciul=[]

	def Tpiszukaj_func(self, arg):
		if arg=='on':
			self.Teleportuj_Do_Kordow_M_()
			self.Auto_Atak_M_()
			self.tpiszukaj.SetText(Przyciskon+'Tp i szukaj')
		elif arg=='off':
			self.Teleportuj_Do_Kordow_M_Stop()
			self.Auto_Atak_M_Stop()
			self.tpiszukaj.SetText(Przyciskoff+'Tp i szukaj')
	def ShowMetinKordy(self):
		self.slotbar_kordyinmet.Show()
		self.BoardAutoMetin.SetSize(340, 130)
	def HideMetinKordy(self):
		self.slotbar_kordyinmet.Hide()
		self.BoardAutoMetin.SetSize(140, 130)

	def WczytajFarmCord(self):
		if os.path.exists('c:montes_cfg/farm_cords.cfg'):
			kordziki = open('c:montes_cfg/farm_cords.cfg', 'r').read().split()
			for x in xrange(len(kordziki)):
				lol = self.kordyinmet.GetText()
				self.kordyinmet.SetText(str(lol+' '+kordziki[x]))


	def ZapiszKordziki(self):
		try:
			os.mkdir('C:montes_cfg')
		except:
			pass
		save = open('c:montes_cfg/farm_cords.cfg', 'w')
		lol = self.kordyinmet.GetText()
		save.write(str(lol))
		save.close()

	def Dodaj_Kordy_Do_Listy(self):
		x, y, z = player.GetMainCharacterPosition()
		x = int(x)/100
		y = int(y)/100
		lol = self.kordyinmet.GetText()
		self.kordyinmet.SetText(str(lol) + ' ' + str(x) + ' ' + str(y))
		self.ZapiszKordziki()

	def Teleportuj_Do_Kordow_M_(self):
		global met,papec,Pozwolenie,teleport_mode,telestep,TeleportState, Debug, GetCurrentMapSize, TeleportToDest, DivideToFloat,ch
		self.Wykrywaczmetinow=XX()
		self.Wykrywaczmetinow.XX1(5)
		self.Wykrywaczmetinow.XX2(self.Teleportuj_Do_Kordow_M_)

		if Pozwolenie == 0:
			if os.path.exists('c:montes_cfg/farm_cords.cfg'):
				kordziki = open('c:montes_cfg/farm_cords.cfg', 'r').read().split()
			My_VID = player.GetMainCharacterIndex()
			x_coordinate1 = int(kordziki[papec])
			y_coordinate1 = int(kordziki[papec+1])
			Position_Xx = int(kordziki[papec])
			Position_Yx = int(kordziki[papec+1])
			myVid = player.GetMainCharacterIndex()
			chr.SelectInstance(myVid)
			self.TeleportToDest((Position_Xx+10)*100,(Position_Yx+10)*100)
			chr.MoveToDestPosition(int(myVid),Position_Xx*100,Position_Yx*100)
			self.Auto_Atak_M_x()
			(My_X1, My_Y1, My_Z1) = chr.GetPixelPosition(myVid)
			My_X1 = int(My_X1 / 100)
			My_Y1 = int(My_Y1 / 100)
			if (My_X1 >= (x_coordinate1)-20 and My_X1 <= (x_coordinate1)+20) and (My_Y1 >= (y_coordinate1)-20 and My_Y1 <= (y_coordinate1)+20):
				if papec != (len(kordziki)):
					papec += 2
				if papec == (len(kordziki)):
					papec = 0
			self.PozycjaText.SetText(str('Pozycja ')+str(papec/2)+str(' / ')+str((len(kordziki)/2)))
	def Teleportuj_Do_Kordow_M_Stop(self):
		self.Wykrywaczmetinow=XX()
		self.Wykrywaczmetinow.XX1(19999999999990)
		self.Wykrywaczmetinow.XX2(self.Teleportuj_Do_Kordow_M_)

	def Auto_Atak_M_x(self):
		global listatypow,TargetVid2,TargetVid,VidyPozwolenie,ListaVidow,ListaVidow2,listash2
		listatypow = []
		Odleglosc = 149
		Moja_Pozycja = player.GetMainCharacterIndex()
		My_VID1 = player.GetMainCharacterIndex()
		(My_X1, My_Y1, My_Z1) = chr.GetPixelPosition(My_VID1)
		My_X1 = int(My_X1 )
		My_Y1 = int(My_Y1 )
		o=player.GetMainCharacterIndex()
		for i in listash2:
			Typ = chr.GetInstanceType(i)
			if chr.HasInstance(i):
				if Typ==2:
					(xm,ym,zm)= chr.GetPixelPosition(i)
					chr.SelectInstance(My_VID1)
					self.TeleportToDest(xm,ym)

	def Auto_Atak_M_(self):
		global listatypow,Pozwolenie,TargetVid2,TargetVid,VidyPozwolenie,ListaVidow,ListaVidow2,listash2
		listatypow = []
		Odleglosc = 149
		Odleglosc1 = []
		teleportek = 1
		self.Wykrywaczmetinow44=XX()
		self.Wykrywaczmetinow44.XX1(1)
		self.Wykrywaczmetinow44.XX2(self.Auto_Atak_M_)
		Moja_Pozycja = player.GetMainCharacterIndex()
		My_VID1 = player.GetMainCharacterIndex()
		(My_X1, My_Y1, My_Z1) = chr.GetPixelPosition(My_VID1)
		My_X1 = int(My_X1 )
		My_Y1 = int(My_Y1 )
		o=player.GetMainCharacterIndex()


		for i in listash2:
			Typ = chr.GetInstanceType(i)
			if chr.HasInstance(i):
				listatypow.append(Typ)
				if listatypow.count(int(2)) == 1:
					Pozwolenie = 1
					teleportek = 0
				if	listatypow.count(int(2))== 0:
					Pozwolenie = 0
					player.SetAttackKeyState(FALSE)
					teleportek = 1
				if listatypow.count(int(2)) >= 2:
					teleportek = 1
					Pozwolenie = 1
			else:
				pass
			if Typ==2:
				dystans = player.GetCharacterDistance(i)
				b = (dystans,i)
				Odleglosc1.append(b)
				Odleglosc1.sort()
				if (Odleglosc1[0][0]) > 150:
					if teleportek == 0:
						x, y, z = chr.GetPixelPosition(Odleglosc1[0][1])
						self.TeleportToDest(int(x+10), int(y+10))
						player.SetAttackKeyState(FALSE)
				else:
					player.SetAttackKeyState(TRUE)


	def Auto_Atak_M_Stop(self):
		global Odleglosc
		self.Wykrywaczmetinow44=XX()
		self.Wykrywaczmetinow44.XX1(19999999999999999999)
		self.Wykrywaczmetinow44.XX2(self.Auto_Atak_M_)
		player.SetAttackKeyState(FALSE)


	def Krzycz(self):
		global ListaRud
		if os.path.exists('c:montes_cfg/Rudy.cfg'):
			kordziki = open('c:montes_cfg/Rudy.cfg', 'r').read().split()
			for x in xrange(len(kordziki)):
				lol = self.KopaczInfo.GetText()
				self.KopaczInfo.SetText(str(lol+' '+kordziki[x]))
				ListaRud.append(kordziki[x])

	def ZapiszRudy(self):
		try:
			os.mkdir('C:montes_cfg')
		except:
			pass
		save = open('c:montes_cfg/Rudy.cfg', 'w')
		lol = self.KopaczInfo.GetText()
		save.write(str(lol))
		save.close()

	def DodajRude_func(self):
		vid = player.GetTargetVID()
		if vid != -1 or vid != 0:
			chr.SelectInstance(vid)
			race=chr.GetRace(vid)
		lol = self.KopaczInfo.GetText()
		self.KopaczInfo.SetText(str(lol)+ ' ' + str(race))
		self.ZapiszRudy()


	def Kop_rude_func(self, arg):
		if arg=='on':
			self.Kop_rude_on()
			self.Krzycz()
			self.Kop_rude.SetText(Przyciskon + 'Kop Rude')
		elif arg=='off':
			self.Kop_rude_off()
			self.Kop_rude.SetText(Przyciskoff + 'Kop Rude')

	def Idz_do_rudy_func(self):
		global ListaRud
		self.Krzycz()
		o=player.GetMainCharacterIndex()
		nrRudy=20047
		if self.Rudzisze.GetCurrentText() == 'Zyla Diamentu':
			nrRudy=20047
		if self.Rudzisze.GetCurrentText() == 'Zyla Bursztynu':
			nrRudy=20048
		if self.Rudzisze.GetCurrentText() == 'Zyla Skamienialego Drewna':
			nrRudy=20049
		if self.Rudzisze.GetCurrentText() == 'Zyla Miedzi':
			nrRudy=20050
		if self.Rudzisze.GetCurrentText() == 'Zyla Srebra':
			nrRudy=20051
		if self.Rudzisze.GetCurrentText() == 'Zyla Zlota':
			nrRudy=20052
		if self.Rudzisze.GetCurrentText() == 'Zyla Jadelitu':
			nrRudy=20053
		if self.Rudzisze.GetCurrentText() == 'Zyla Ebonitu':
			nrRudy=20054
		if self.Rudzisze.GetCurrentText() == 'Zyla Sterta Muszli':
			nrRudy=20055
		if self.Rudzisze.GetCurrentText() == 'Zyla Bialego Zlota':
			nrRudy=20056
		if self.Rudzisze.GetCurrentText() == 'Zyla Krysztalu':
			nrRudy=20057
		if self.Rudzisze.GetCurrentText() == 'Zyla Ametystu':
			nrRudy=20058
		if self.Rudzisze.GetCurrentText() == 'Zyla Nieb. Lez':
			nrRudy=20059

		if self.Rudzisze.GetCurrentText() == 'Wlasne Rudy':
			for i in xrange(o-50000, o+52000):
				a = chr.GetInstanceType(i)
				if a == 1:
					chr.SelectInstance(i)
					Race=chr.GetRace(i)
					for lol in ListaRud:
						if Race==int(lol):
							(X, Y, Z) = chr.GetPixelPosition(i)
							Moja_Pozycja = player.GetMainCharacterIndex()
							if self.Rudzisze1.GetCurrentText() == 'Idz':
								chr.MoveToDestPosition(int(Moja_Pozycja),X+100,Y+100)
							if self.Rudzisze1.GetCurrentText() == 'Teleportuj':
								self.TeleportToDest(int(X+100),int(Y+100))
		if self.Rudzisze.GetCurrentText() != 'Wlasne Rudy':
			for i in xrange(o-50000, o+52000):
					a = chr.GetInstanceType(i)
					if a == 1:
						chr.SelectInstance(i)
						Race=chr.GetRace(i)
						if Race==nrRudy:
							(X, Y, Z) = chr.GetPixelPosition(i)
							Moja_Pozycja = player.GetMainCharacterIndex()
							if self.Rudzisze1.GetCurrentText() == 'Idz':
								chr.MoveToDestPosition(int(Moja_Pozycja),X+100,Y+100)
							if self.Rudzisze1.GetCurrentText() == 'Teleportuj':
								self.TeleportToDest(int(X+100),int(Y+100))

	def Kop_rude_on(self):
		global ListaRud
		self.Krzycz()
		czaskop = self.Kopacztime.GetText()
		self.Kopaczej=XX()
		self.Kopaczej.XX1(int(czaskop))
		self.Kopaczej.XX2(self.Kop_rude_on)
		o=player.GetMainCharacterIndex()
		nrRudy=20047
		if self.Rudzisze.GetCurrentText() == 'Zyla Diamentu':
			nrRudy=20047
		if self.Rudzisze.GetCurrentText() == 'Zyla Bursztynu':
			nrRudy=20048
		if self.Rudzisze.GetCurrentText() == 'Zyla Skamienialego Drewna':
			nrRudy=20049
		if self.Rudzisze.GetCurrentText() == 'Zyla Miedzi':
			nrRudy=20050
		if self.Rudzisze.GetCurrentText() == 'Zyla Srebra':
			nrRudy=20051
		if self.Rudzisze.GetCurrentText() == 'Zyla Zlota':
			nrRudy=20052
		if self.Rudzisze.GetCurrentText() == 'Zyla Jadelitu':
			nrRudy=20053
		if self.Rudzisze.GetCurrentText() == 'Zyla Ebonitu':
			nrRudy=20054
		if self.Rudzisze.GetCurrentText() == 'Zyla Sterta Muszli':
			nrRudy=20055
		if self.Rudzisze.GetCurrentText() == 'Zyla Bialego Zlota':
			nrRudy=20056
		if self.Rudzisze.GetCurrentText() == 'Zyla Krysztalu':
			nrRudy=20057
		if self.Rudzisze.GetCurrentText() == 'Zyla Ametystu':
			nrRudy=20058
		if self.Rudzisze.GetCurrentText() == 'Zyla Nieb. Lez':
			nrRudy=20059

		if self.Rudzisze.GetCurrentText() == 'Wlasne Rudy':
			for i in xrange(o-50000, o+52000):
				dystans = player.GetCharacterDistance(i)
				Typ = chr.GetInstanceType(i)
				if Typ==1:
					chr.SelectInstance(i)
					Race=chr.GetRace(i)
					for lol in ListaRud:
						if Race==int(lol):
							if dystans < 150:
								chr.SelectInstance(i)
								net.SendOnClickPacket(i)
							else:
								self.Idz_do_rudy_func()
		if self.Rudzisze.GetCurrentText() != 'Wlasne Rudy':
			for i in xrange(o-50000, o+52000):
				dystans = player.GetCharacterDistance(i)
				Typ = chr.GetInstanceType(i)
				if Typ==1:
					chr.SelectInstance(i)
					Race=chr.GetRace(i)
					if Race==nrRudy:
						if dystans < 150:
							chr.SelectInstance(i)
							net.SendOnClickPacket(i)
						else:
							self.Idz_do_rudy_func()
	def Kop_rude_off(self):
		self.Kopaczej=XX()
		self.Kopaczej.XX1(9999999999999999999999990)
		self.Kopaczej.XX2(self.Kop_rude_on)

	def Set_Rozdzielanie_Slot(self):
		global SlotDoDzielenia
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()

			SlotDoDzielenia = mouseModule.mouseController.GetAttachedSlotNumber()
			item.SelectItem(attachedSlotVnum)

		item.SelectItem(int(attachedSlotVnum))
		self.RozdzielanieSlotIcon.LoadImage(str(item.GetIconImageFileName()))
		mouseModule.mouseController.DeattachObject()

	def Rozdziel_func(self):
		global SlotDoDzielenia
		IloscStacku = (float(self.PoIleRozdzielicIn.GetText()))
		for i in xrange(player.INVENTORY_PAGE_SIZE*5):
			if player.GetItemIndex(i) == 0:
				net.SendItemMovePacket(SlotDoDzielenia, i, IloscStacku)

	def Tp1_func(self):
		global kordyx
		if kordyx[0] and kordyx[1] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[0])*100,int(kordyx[1])*100)

	def Tp2_func(self):
		global kordyx
		if kordyx[2] and kordyx[3] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[2])*100,int(kordyx[3])*100)

	def Tp3_func(self):
		global kordyx
		if kordyx[4] and kordyx[5] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[4])*100,int(kordyx[5])*100)

	def Tp4_func(self):
		global kordyx
		if kordyx[6] and kordyx[7] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[6])*100,int(kordyx[7])*100)

	def Tp5_func(self):
		global kordyx
		if kordyx[8] and kordyx[9] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[8])*100,int(kordyx[9])*100)

	def Tp6_func(self):
		global kordyx
		if kordyx[10] and kordyx[11] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[10])*100,int(kordyx[11])*100)

	def Tp7_func(self):
		global kordyx
		if kordyx[12] and kordyx[13] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[12])*100,int(kordyx[13])*100)

	def Tp8_func(self):
		global kordyx
		if kordyx[14] and kordyx[15] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[14])*100,int(kordyx[15])*100)

	def Tp9_func(self):
		global kordyx
		if kordyx[16] and kordyx[17] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[16])*100,int(kordyx[17])*100)

	def Tp10_func(self):
		global kordyx
		if kordyx[18] and kordyx[19] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[18])*100,int(kordyx[19])*100)

	def Tp11_func(self):
		global kordyx
		if kordyx[20] and kordyx[21] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[20])*100,int(kordyx[21])*100)

	def Tp12_func(self):
		global kordyx
		if kordyx[22] and kordyx[23] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[22])*100,int(kordyx[23])*100)

	def Tp13_func(self):
		global kordyx
		if kordyx[24] and kordyx[25] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[24])*100,int(kordyx[25])*100)

	def Tp14_func(self):
		global kordyx
		if kordyx[26] and kordyx[27] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[26])*100,int(kordyx[27])*100)

	def Tp15_func(self):
		global kordyx
		if kordyx[28] and kordyx[29] == '0':
			chat.AppendChat(2, 'Brak zapisu pozycji')
		else:
			self.TeleportToDest(int(kordyx[28])*100,int(kordyx[29])*100)

	def ZapiszKordzikiZap(self):
		global kordyx

		try:
			os.mkdir('C:montes_cfg')
		except:
			pass
		save = open('c:montes_cfg/Tp_kordy.cfg', 'w')

		x = (str(kordyx[0])+' '+
		str(kordyx[1])+' '+
		str(kordyx[2])+' '+
		str(kordyx[3])+' '+
		str(kordyx[4])+' '+
		str(kordyx[5])+' '+
		str(kordyx[6])+' '+
		str(kordyx[7])+' '+
		str(kordyx[8])+' '+
		str(kordyx[9])+' '+
		str(kordyx[10])+' '+
		str(kordyx[11])+' '+
		str(kordyx[12])+' '+
		str(kordyx[13])+' '+
		str(kordyx[14])+' '+
		str(kordyx[15])+' '+
		str(kordyx[16])+' '+
		str(kordyx[17])+' '+
		str(kordyx[18])+' '+
		str(kordyx[19])+' '+
		str(kordyx[20])+' '+
		str(kordyx[21]))
		xx  = (str(kordyx[22])+' '+
		str(kordyx[23])+' '+
		str(kordyx[24])+' '+
		str(kordyx[25])+' '+
		str(kordyx[26])+' '+
		str(kordyx[27])+' '+
		str(kordyx[28])+' '+
		str(kordyx[29]))
		xxx = (str(kordyx[30])+' '+
		str(kordyx[31])+' '+
		str(kordyx[32])+' '+
		str(kordyx[33])+' '+
		str(kordyx[34])+' '+
		str(kordyx[35])+' '+
		str(kordyx[36])+' '+
		str(kordyx[37])+' '+
		str(kordyx[38])+' '+
		str(kordyx[39])+' '+
		str(kordyx[40])+' '+
		str(kordyx[41])+' '+
		str(kordyx[42])+' '+
		str(kordyx[43])+' '+
		str(kordyx[44]))

		save.write(str(x+' '+xx+' '+xxx))
		save.close()

	def Loadfff(self):
		global kordyx
		if os.path.exists('c:montes_cfg/Tp_kordy.cfg'):
			kordziki = open('c:montes_cfg/Tp_kordy.cfg', 'r').read().split()

			for t in range(45):
				kordyx[t] = kordziki[t]

			for k in range(30,45):
				kordziki[k] = kordziki[k].replace('_',' ')




			self.Tp1.SetToolTipText(str('x: ') + str(kordziki[0]) + str(' y: ') + str(kordziki[1]))
			self.Tp1.SetText(str(kordziki[30]))
			self.Tp2.SetToolTipText(str('x: ') + str(kordziki[2]) + str(' y: ') + str(kordziki[3]))
			self.Tp2.SetText(str(kordziki[31]))
			self.Tp3.SetToolTipText(str('x: ') + str(kordziki[4]) + str(' y: ') + str(kordziki[5]))
			self.Tp3.SetText(str(kordziki[32]))
			self.Tp4.SetToolTipText(str('x: ') + str(kordziki[6]) + str(' y: ') + str(kordziki[7]))
			self.Tp4.SetText(str(kordziki[33]))
			self.Tp5.SetToolTipText(str('x: ') + str(kordziki[8]) + str(' y: ') + str(kordziki[9]))
			self.Tp5.SetText(str(kordziki[34]))
			self.Tp6.SetToolTipText(str('x: ') + str(kordziki[10]) + str(' y: ') + str(kordziki[11]))
			self.Tp6.SetText(str(kordziki[35]))
			self.Tp7.SetToolTipText(str('x: ') + str(kordziki[12]) + str(' y: ') + str(kordziki[13]))
			self.Tp7.SetText(str(kordziki[36]))
			self.Tp8.SetToolTipText(str('x: ') + str(kordziki[14]) + str(' y: ') + str(kordziki[15]))
			self.Tp8.SetText(str(kordziki[37]))
			self.Tp9.SetToolTipText(str('x: ') + str(kordziki[16]) + str(' y: ') + str(kordziki[17]))
			self.Tp9.SetText(str(kordziki[38]))
			self.Tp10.SetToolTipText(str('x: ') + str(kordziki[18]) + str(' y: ') + str(kordziki[19]))
			self.Tp10.SetText(str(kordziki[39]))
			self.Tp11.SetToolTipText(str('x: ') + str(kordziki[20]) + str(' y: ') + str(kordziki[21]))
			self.Tp11.SetText(str(kordziki[40]))
			self.Tp12.SetToolTipText(str('x: ') + str(kordziki[22]) + str(' y: ') + str(kordziki[23]))
			self.Tp12.SetText(str(kordziki[41]))
			self.Tp13.SetToolTipText(str('x: ') + str(kordziki[24]) + str(' y: ') + str(kordziki[25]))
			self.Tp13.SetText(str(kordziki[42]))
			self.Tp14.SetToolTipText(str('x: ') + str(kordziki[26]) + str(' y: ') + str(kordziki[27]))
			self.Tp14.SetText(str(kordziki[43]))
			self.Tp15.SetToolTipText(str('x: ') + str(kordziki[28]) + str(' y: ') + str(kordziki[29]))
			self.Tp15.SetText(str(kordziki[44]))

	def uuuiii(self):
		global listash,ttt,pozwolenieLISTY,CURMAP,listash2
		listash.sort()
		if ttt==100:
			ttt=0
			golgol = listash[len(listash)-1]
			listash=[]
			listash.append(golgol)

		if pozwolenieLISTY == 0:
			targetvid=player.GetMainCharacterIndex()
		else:
			if player.GetMainCharacterIndex() <listash[len(listash)-1]:
				targetvid=listash[len(listash)-1]
			else:
				targetvid=player.GetMainCharacterIndex()
		for i in xrange(targetvid-(ttt*3000)+50000, targetvid-(ttt*3000)+53000):
			dystans = player.GetCharacterDistance(i)
			a = chr.GetInstanceType(i)
			if a==2 or a==0 and dystans>=0:
				listash.append(i)
		ttt=ttt+1
		if len(listash) > 0:
			pozwolenieLISTY = 1
		else:
			pozwolenieLISTY = 0


		for i in listash:
			if i in listash2:
				pass
			else:
				dystans = player.GetCharacterDistance(i)
				if dystans>=0:
					listash2.append(i)
		for i in listash2:
			dystans = player.GetCharacterDistance(i)
			if dystans>=0:
				pass
			else:
				listash2.remove(i)

		if background.GetCurrentMapName() != CURMAP:
			listash=[player.GetMainCharacterIndex()]
			ttt = 0
			pozwolenieLISTY = 0
		CURMAP = background.GetCurrentMapName()
		self.uuuiiiczas=XX()
		self.uuuiiiczas.XX1(0.004)
		self.uuuiiiczas.XX2(self.uuuiii)

	def Zapisz_funcZap(self):
		global kordyx
		(PlayerX, PlayerY, PlayerZ) = player.GetMainCharacterPosition()
		x = self.Zapcombo.GetCurrentText()
		y = self.NazwaZapisu.GetText()
		PlayerX = int(PlayerX)/100
		PlayerY = int(PlayerY)/100
		yy = y.replace(' ','_')
		if x == '1':
			kordyx[0]=PlayerX
			kordyx[1]=PlayerY
			kordyx[30]=yy
			self.Tp1.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp1.SetText(str(y))
		if x == '2':
			kordyx[2]=PlayerX
			kordyx[3]=PlayerY
			kordyx[31]=yy
			self.Tp2.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp2.SetText(str(y))
		if x == '3':
			kordyx[4]=PlayerX
			kordyx[5]=PlayerY
			kordyx[32]=yy
			self.Tp3.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp3.SetText(str(y))
		if x == '4':
			kordyx[6]=PlayerX
			kordyx[7]=PlayerY
			kordyx[33]=yy
			self.Tp4.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp4.SetText(str(y))
		if x == '5':
			kordyx[8]=PlayerX
			kordyx[9]=PlayerY
			kordyx[34]=yy
			self.Tp5.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp5.SetText(str(y))
		if x == '6':
			kordyx[10]=PlayerX
			kordyx[11]=PlayerY
			kordyx[35]=yy
			self.Tp6.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp6.SetText(str(y))
		if x == '7':
			kordyx[12]=PlayerX
			kordyx[13]=PlayerY
			kordyx[36]=yy
			self.Tp7.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp7.SetText(str(y))
		if x == '8':
			kordyx[14]=PlayerX
			kordyx[15]=PlayerY
			kordyx[37]=yy
			self.Tp8.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp8.SetText(str(y))
		if x == '9':
			kordyx[16]=PlayerX
			kordyx[17]=PlayerY
			kordyx[38]=yy
			self.Tp9.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp9.SetText(str(y))
		if x == '10':
			kordyx[18]=PlayerX
			kordyx[19]=PlayerY
			kordyx[39]=yy
			self.Tp10.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp10.SetText(str(y))
		if x == '11':
			kordyx[20]=PlayerX
			kordyx[21]=PlayerY
			kordyx[40]=yy
			self.Tp11.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp11.SetText(str(y))
		if x == '12':
			kordyx[22]=PlayerX
			kordyx[23]=PlayerY
			kordyx[41]=yy
			self.Tp12.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp12.SetText(str(y))
		if x == '13':
			kordyx[24]=PlayerX
			kordyx[25]=PlayerY
			kordyx[42]=yy
			self.Tp13.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp13.SetText(str(y))
		if x == '14':
			kordyx[26]=PlayerX
			kordyx[27]=PlayerY
			kordyx[43]=yy
			self.Tp14.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp14.SetText(str(y))
		if x == '15':
			kordyx[28]=PlayerX
			kordyx[29]=PlayerY
			kordyx[44]=yy
			self.Tp15.SetToolTipText(str('x: ') + str(PlayerX) + str(' y: ') + str(PlayerY))
			self.Tp15.SetText(str(y))

		self.ZapiszKordzikiZap()





	def OddExpGildia_func(self, arg):
		if arg=='on':
			self.OddawajExpa_FuncON()
			self.OddawajExpBtn.SetText(Przyciskon + 'Oddawaj Expa')
		elif arg=='off':
			self.OddawajExpa_FuncOFF()
			self.OddawajExpBtn.SetText(Przyciskoff + 'Oddawaj Expa')


	def OddawajExpa_FuncON(self):
		if player.GetStatus(player.EXP) > 100:
			net.SendGuildOfferPacket(int(player.GetStatus(player.EXP)))


		self.OddawajExpabl = XX()
		self.OddawajExpabl.XX1(float(0.1))
		self.OddawajExpabl.XX2(self.OddawajExpa_FuncON)

	def OddawajExpa_FuncOFF(self):
		self.OddawajExpabl = XX()
		self.OddawajExpabl.XX1(float(9999999999999))
		self.OddawajExpabl.XX2(self.OddawajExpa_FuncOFF)

	def zrobgildie(self):
		opop = self.NazwagildicIn.GetText()
		IloscStacku1 = (str(opop))
		net.SendAnswerMakeGuildPacket(IloscStacku1)

	def Usuninfoitem(self):
		global idii
		idii = 0
		for xx in xrange(3):
			self.givesii.ClearSlot(xx)
		self.givesii.RefreshSlot()
		self.BoardItemInfo.SetSize(350, 290)

	def MpcMontes_func(self):
		os.startfile('https://www.mpcforum.pl/profile/121805-fanmetin2/')

	def MpcKag_func(self):
		os.startfile('www.mpcforum.pl/user/1374994-kag321/')

	def YTMontes_func(self):
		os.startfile('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

	def GGMontes_func(self):
		os.startfile('gg-99999999')

	def Ulepsz_Item(self):
		global SlotUlepszania
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()

			SlotUlepszania = mouseModule.mouseController.GetAttachedSlotNumber()
			item.SelectItem(attachedSlotVnum)

		item.SelectItem(int(attachedSlotVnum))
		self.UlepszanieSlotIcon.LoadImage(str(item.GetIconImageFileName()))
		mouseModule.mouseController.DeattachObject()

	def SlotUleDo(self):
		global SlotUlepszaniaDO
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()

			SlotUlepszaniaDO = attachedSlotVnum
			item.SelectItem(attachedSlotVnum)

		item.SelectItem(int(attachedSlotVnum))
		self.UlepszanieSlotIconx.LoadImage(str(item.GetIconImageFileName()))
		mouseModule.mouseController.DeattachObject()

	def ooo(self):
		shop.GetOfflineShopItemPrice=shop.GetItemPrice
		shop.GetOfflineShopItemCount=shop.GetItemCount
		shop.GetOfflineShopItemID=shop.GetItemID
		shop.IsOfflineShop=shop.IsPrivateShop
		shop.OFFLINE_SHOP_SLOT_COUNT=shop.SHOP_SLOT_COUNT
		net.SendOfflineShopEndPacket=net.SendShopEndPacket



	def PotyStartFunc1(self):
		self.Skan.SetText(Przyciskon+'Skanuj')
		global listash,kukloma,cos,costam,listakag,listakordy
		self.autopotystartfunkacjaczas=XX()
		self.autopotystartfunkacjaczas.XX1(0.05)
		self.autopotystartfunkacjaczas.XX2(self.PotyStartFunc1)
		o=player.GetMainCharacterIndex()
		if kukloma==0:
			listash=[]
			listakag=[]
			listakordy=[]

			for i in xrange(1, o+100000):
				dystans = player.GetCharacterDistance(i)
				if dystans > 0 :
					a = chr.GetInstanceType(i)
					chr.SelectInstance(i)
					b=chr.GetRace(i)
					if (a==6 or a==1) and b==30000:
						imie=chr.GetNameByVID(i)
						listash.append([i,str(imie)])
		if kukloma>0 and kukloma <= len(listash):
			if shop.IsOfflineShop()==0:
				net.SendOnClickPacket(listash[kukloma-1][0])
				costam=costam+1
				if costam==50:
					kukloma=kukloma+1
					costam=0
			if shop.IsOfflineShop()==1:
				costam=0
				b=0
				for i in xrange(shop.OFFLINE_SHOP_SLOT_COUNT):
					if shop.GetOfflineShopItemPrice(i)>0:
						if b==0:
							a=i
							b=b+1

						if kukloma>1 and len(listash[kukloma-2])>2 and shop.GetOfflineShopItemPrice(a)==listash[kukloma-2][2]:
							if shop.GetOfflineShopItemCount(i)==listash[kukloma-2][3]:
								if shop.GetOfflineShopItemID(i)==listash[kukloma-2][4]:
									if cos<50:

										cos=cos+1
										break
									if cos==50:
										cos=50

						listash[kukloma-1].append(shop.GetOfflineShopItemPrice(i))
						listash[kukloma-1].append(shop.GetOfflineShopItemCount(i))
						listash[kukloma-1].append(shop.GetOfflineShopItemID(i))
						listash[kukloma-1].append(item.GetItemName(item.SelectItem(shop.GetOfflineShopItemID(i))))
						Cenazajeden1 = shop.GetOfflineShopItemPrice(i) / shop.GetOfflineShopItemCount(i)
						Cenazajeden = format(Cenazajeden1,',d')
						Cenazajeden = Cenazajeden.replace(',','.')
						NazwaItemku = item.GetItemName(item.SelectItem(shop.GetOfflineShopItemID(i)))
						Ilosc = shop.GetOfflineShopItemCount(i)
						ID = shop.GetOfflineShopItemID(i)
						Vid = listash[kukloma-1][0]
						NazwaSklepu = listash[kukloma-1][1]
						ddf =(Cenazajeden,NazwaItemku,Ilosc,ID,Vid,NazwaSklepu,Cenazajeden1)

						listakag.append(ddf)


					if i==shop.OFFLINE_SHOP_SLOT_COUNT-1:
						kukloma=kukloma+1
						cos=0
				net.SendOfflineShopEndPacket()

		if kukloma >= len(listash):
			kukloma = kukloma+1

		if kukloma==0:
			kukloma=1
			cos=1


	def autopotystopfunkcja(self):
		self.Skan.SetText(Przyciskoff+'Skanuj')
		self.autopotystartfunkacjaczas=XX()
		self.autopotystartfunkacjaczas.XX1(100000000.0)
		self.autopotystartfunkacjaczas.XX2(self.PotyStartFunc1)
		global listash,kukloma,cos,costam,listakag,listaWysz
		costam=0
		listakag.sort(key=uno,reverse=True)
		listaWysz= []
		listaWysz.sort(key=uno,reverse=True)
		kukloma=0
		cos=0

		self.gui = {
				'scrollbar' : self.CreateScrollbar(self.ShopScannerBoard,415,369,85),
				'boards' : []
				}

		for i in xrange(min(7,len(listakag))):
			for l in xrange(len(listakag)):
				if self.liniecos.GetText()!='' and str(listakag[l][1])[:len(self.liniecos.GetText())]==self.liniecos.GetText():
					listaWysz.append(listakag[l])
					self.gui['scrollbar'].SetMiddleBarSize(float(2) / float(len(listaWysz)))
					self.gui['scrollbar'].Show()
					self.gui['scrollbar'].SetScrollEvent(self.__OnScroll)
				elif self.liniecos.GetText()=='':
					listaWysz=listakag
					self.gui['scrollbar'].SetMiddleBarSize(float(2) / float(len(listaWysz)))
					self.gui['scrollbar'].Show()
					self.gui['scrollbar'].SetScrollEvent(self.__OnScroll)
		for k in range(min(7,len(listaWysz))):
			self.gui['boards'].append(ExampleBoard(self.ShopScannerBoard, 10, 80 + 60 * k))
			self.gui['boards'][k].SetBoardInfo(k, listaWysz[k][0], listaWysz[k][2], listaWysz[k][1])
	def __OnScroll(self):
		board_count = len(self.gui['boards'])
		pos = int(self.gui['scrollbar'].GetPos() * (len(listaWysz) - 7))
		for l in xrange(board_count):
			realPos = l + pos
			self.gui['boards'][l].SetBoardInfo(realPos, listaWysz[realPos][0], listaWysz[realPos][2], listaWysz[realPos][1])
	def CreateScrollbar(self, parent, height, x, y):
		scrollbar = ui.ScrollBar()
		scrollbar.SetParent(parent)
		scrollbar.SetScrollBarSize(height)
		scrollbar.SetPosition(x, y)
		scrollbar.Show()
		return scrollbar

	def ZatwCelu_func(self):
		global targecik
		targecik=int(player.GetTargetVID())
		NickBuffBot=chr.GetNameByVID(player.GetTargetVID())
		self.CelBuff = self.comp.TextLine(self.BoardBuffbot, 'Cel - ' + NickBuffBot, 20, 40, self.comp.RGB(255, 255, 0),Czciaka)


	def BlogoBuffBot_func(self, arg):
		if arg=='on':
			global blogopoz
			blogopoz = 0
		elif arg=='off':
			blogopoz = 1
	def PomocBuffBot_func(self, arg):
		if arg=='on':
			global pomocpoz
			pomocpoz = 0
		elif arg=='off':
			pomocpoz = 1
	def OdbicieBuffBot_func(self, arg):
		if arg=='on':
			global odbiciepoz
			odbiciepoz = 0
		elif arg=='off':
			odbiciepoz = 1

	def StartBuffBot_func(self, arg):
		if arg=='on':
			self.StartBuffBot_func1()
			self.StartBuffBot.SetText(Przyciskon+'Start')
		elif arg=='off':
			self.StartBuffBot_func1OFF()
			self.StartBuffBot.SetText(Przyciskoff+'Start')

	def StartBuffBot_func1(self):
		global targecik,blogopoz,odbiciepoz,pomocpoz
		self.BuffBot=XX()
		self.BuffBot.XX1(int(1))
		self.BuffBot.XX2(self.StartBuffBot_func1)
		player.SetTarget(int(targecik))
		player.OpenCharacterMenu(int(targecik))
		if blogopoz == 0:
			if player.IsSkillCoolTime(4) == 0:
					player.ClickSkillSlot(4)
		if pomocpoz == 0:
			if player.IsSkillCoolTime(6) == 0:
					player.ClickSkillSlot(6)
		if odbiciepoz == 0:
			if player.IsSkillCoolTime(5) == 0:
					player.ClickSkillSlot(5)


	def StartBuffBot_func1OFF(self):
		self.BuffBot=XX()
		self.BuffBot.XX1(99999999999)
		self.BuffBot.XX2(self.StartBuffBot_func1)


	def ZapiszUstawienia(self):
		global Dopalacz_ID,Mobber_ID,Poty_1_ID,Poty_2_ID,Dopalacz_ID,Slotlista
		try:
			os.mkdir('C:montes_cfg')
		except:
			pass

		open('c:montes_cfg/montes_cfg.cfg', 'w')
		x = (str(Slotlista[0])+' '+
		str(Dopalacz_ID[0])+' '+
		str(Slotlista[1])+' '+
		str(Dopalacz_ID[1])+' '+
		str(Slotlista[2])+' '+
		str(Dopalacz_ID[2])+' '+
		str(Slotlista[3])+' '+
		str(Dopalacz_ID[3])+' '+
		str(Slotlista[4])+' '+
		str(Dopalacz_ID[4])+' '+
		str(Slotlista[5])+' '+
		str(Dopalacz_ID[5])+' '+
		str(Slotlista[6])+' '+
		str(Dopalacz_ID[6])+' '+
		str(Slotlista[7])+' '+
		str(Dopalacz_ID[7])+' '+
		str(Slotlista[8])+' '+
		str(Dopalacz_ID[8])+' '+
		str(Slotlista[9])+' '+
		str(Dopalacz_ID[9])+' '+
		str(Slotlista[10])+' '+
		str(Dopalacz_ID[10]))
		xx  = (str(Slotlista[11])+' '+
		str(Dopalacz_ID[11])+' '+
		str(Slotlista[12])+' '+
		str(Dopalacz_ID[12])+' '+
		str(Slotlista[13])+' '+
		str(Dopalacz_ID[13])+' '+
		str(Slotlista[14])+' '+
		str(Dopalacz_ID[14])+' '+
		str(Slotlista[15])+' '+
		str(Dopalacz_ID[15])+' '+
		str(Slotlista[16])+' '+
		str(Dopalacz_ID[16])+' '+
		str(Slotlista[17])+' '+
		str(Dopalacz_ID[17])+' '+
		str(Slotlista[18])+' '+
		str(Dopalacz_ID[18])+' '+
		str(Slotlista[19])+' '+
		str(Dopalacz_ID[19])+' '+
		str(Slotlista[20])+' '+
		str(Dopalacz_ID[20])+' '+
		str(Slotlista[21])+' '+
		str(Dopalacz_ID[21]))
		xxx = (str(Slotlista[22])+' '+
		str(Dopalacz_ID[22])+' '+
		str(Slotlista[23])+' '+
		str(Dopalacz_ID[23])+' '+
		str(Slotlista[24])+' '+
		str(Dopalacz_ID[24])+' '+
		str(Slotlista[25])+' '+
		str(Dopalacz_ID[25])+' '+
		str(Slotlista[26])+' '+
		str(Dopalacz_ID[26])+' '+
		str(Slotlista[27])+' '+
		str(Dopalacz_ID[27]))
		xxxx = (str(self.Coiledopyin.GetText())+' '+
		str(Mobber_ID)+' '+
		str(self.Peleczas.GetText())+' '+
		str(Poty_1_ID)+' '+
		str(self.Potyhpczas.GetText())+' '+
		str(Poty_2_ID)+' '+
		str(self.Potympczas.GetText()))

		open('c:montes_cfg/montes_cfg.cfg', 'w').write(str(x+' '+xx+' '+xxx+' '+xxxx))
		chat.AppendChat(chat.BOARD_STATE_LOG,'Zapisano ustawienia')

	def WczytajUstawienia(self):
		global Dopalacz_ID,Mobber_ID,Poty_1_ID,Poty_2_ID
		global Slotlista,cfg,xox,Dopalacz_ID
		self.Krzycz()
		self.Krzycz1()
		self.WczytajFarmCord()
		self.Loadfff()
		if os.path.exists('c:montes_cfg/montes_cfg.cfg'):
			cfg = open('c:montes_cfg/montes_cfg.cfg', 'r').read().split()
			y = 1
			z = 0
			for x in xrange(0,28):
				Dopalacz_ID[x] = cfg[y]
				Slotlista[x] = cfg[z]
				self.gives.SetItemSlot(int(cfg[z]), int(cfg[y]))
				y = y + 2
				z = z + 2
				if y >= 56:
					break

			self.Coiledopyin.SetText(str(cfg[56]))

			Mobber_ID = cfg[57]

			if Mobber_ID == '0':
				self.MobberSlotIcon.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
			else:
				item.SelectItem(int(Mobber_ID))
				self.MobberSlotIcon.LoadImage(str(item.GetIconImageFileName()))

			self.Peleczas.SetText(str(cfg[58]))

			Poty_1_ID = int(cfg[59])

			if Poty_1_ID == '0':
				self.PotySlotIcon.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
			else:
				item.SelectItem(int(Poty_1_ID))
				self.PotySlotIcon.LoadImage(str(item.GetIconImageFileName()))

			self.Potyhpczas.SetText(str(cfg[60]))

			Poty_2_ID = int(cfg[61])

			if Poty_2_ID == '0':
				self.PotySlotIcon2.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
			else:
				item.SelectItem(int(Poty_2_ID))
				self.PotySlotIcon2.LoadImage(str(item.GetIconImageFileName()))

			self.Potympczas.SetText(str(cfg[62]))

			chat.AppendChat(2, 'Wczytano ustawienia')

	def usunrade(self):
		global Rada_ID
		Rada_ID = 0
		self.RadySlotIcon.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')

	def usunegzo(self):
		global Egzo_ID
		Egzo_ID = 0
		self.EgzoSlotIcon.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')

	def usunku(self):
		global KU_ID
		KU_ID = 0
		self.KUSloticon.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')

	def RadySlotFunc(self):
		global Rada_ID
		Rada_ID = 0
		if mouseModule.mouseController.isAttached():
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			item.SelectItem(attachedSlotVnum)

			Rada_ID = mouseModule.mouseController.GetAttachedItemIndex()
			mouseModule.mouseController.DeattachObject()

			item.SelectItem(int(attachedSlotVnum))
			self.RadySlotIcon.LoadImage(str(item.GetIconImageFileName()))

	def EgzoSlotFunc(self):
		global Egzo_ID
		Egzo_ID = 0
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()

			Egzo_ID = mouseModule.mouseController.GetAttachedItemIndex()
			item.SelectItem(attachedSlotVnum)

		item.SelectItem(int(attachedSlotVnum))
		self.EgzoSlotIcon.LoadImage(str(item.GetIconImageFileName()))
		mouseModule.mouseController.DeattachObject()


	def KuSlotFunc(self):
		global KU_ID
		KU_ID = 0
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()

			KU_ID = mouseModule.mouseController.GetAttachedItemIndex()
			item.SelectItem(attachedSlotVnum)

		item.SelectItem(int(attachedSlotVnum))
		self.KUSloticon.LoadImage(str(item.GetIconImageFileName()))
		mouseModule.mouseController.DeattachObject()

	def Witplus_func(self):
		for x in xrange(int(self.Witin.GetText())):
			oldSendChatPacket('/stat ht')

	def Intplus_func(self):
		for x in xrange(int(self.Intin.GetText())):
			oldSendChatPacket('/stat iq')

	def Silaplus_func(self):
		for x in xrange(int(self.Silain.GetText())):
			oldSendChatPacket('/stat st')

	def Zreplus_func(self):
		for x in xrange(int(self.Zrein.GetText())):
			oldSendChatPacket('/stat dx')

	def Czytaj_func(self, arg):
		if arg=='on':
			self.CzytajkaStart()
			self.Czytaj.SetText(Przyciskon+'Czytaj')
		elif arg=='off':
			self.CzytajkaStop()
			self.Czytaj.SetText(Przyciskoff+'Czytaj')

	def CzytajkaStart(self):
		global Rada_ID,Egzo_ID,KU_ID
		for i in xrange(player.INVENTORY_PAGE_SIZE*5):
			Rada_IDX = player.GetItemIndex(i)
			if Rada_IDX == (int(Rada_ID)):
				net.SendItemUsePacket(i)
				break

		for i in xrange(player.INVENTORY_PAGE_SIZE*5):
			Egzo_IDX = player.GetItemIndex(i)
			if Egzo_IDX == (int(Egzo_ID)):
				net.SendItemUsePacket(i)
				break

		for i in xrange(player.INVENTORY_PAGE_SIZE*5):
			KU_IDX = player.GetItemIndex(i)
			if KU_IDX == (int(KU_ID)):
				net.SendItemUsePacket(i)
				break

		self.Czytelniczek = XX()
		self.Czytelniczek.XX1(float(0.1))
		self.Czytelniczek.XX2(self.CzytajkaStart)

	def CzytajkaStop(self):
		self.Czytelniczek = XX()
		self.Czytelniczek.XX1(float(0.1))
		self.Czytelniczek.XX2(self.CzytajkaStop)


	def lowienie_func(self, arg):
		if arg=='on':
			self.StartFishBot()
			self.StartFishBotg()

		elif arg=='off':
			self.StopFishBot()

	def StartFishBotg(self):
		if self.state == 'start':
			if self.ProcessTimeStamp + 6.0 < app.GetTime():
				if self.AddBait():
					player.SetAttackKeyState(TRUE)
					player.SetAttackKeyState(FALSE)
					self.ProcessTimeStamp = app.GetTime()
					self.state = 'waiting'
		if self.state == 'action':
			if self.ProcessTimeStamp + self.time < app.GetTime():
				player.SetAttackKeyState(TRUE)
				player.SetAttackKeyState(FALSE)
				self.ProcessTimeStamp = app.GetTime()
				self.state = 'start'
		if self.state == 'waiting':
			if not chrmgr.IsPossibleEmoticon(-1):
				self.ProcessTimeStamp = app.GetTime() + float(self.RandomTolerance())
				self.state = 'action'
			if self.ProcessTimeStamp + 48.0 < app.GetTime():
				self.ProcessTimeStamp = app.GetTime()
				self.state = 'start'

		self.StartFishBotx = XX()
		self.StartFishBotx.XX1(float(0.001))
		self.StartFishBotx.XX2(self.StartFishBotg)

	def StartFishBot(self):
		self.time = float(self.lowienieczas.GetText())
		if self.AddBait():
			player.SetAttackKeyState(TRUE)
			player.SetAttackKeyState(FALSE)
			self.ProcessTimeStamp = app.GetTime()
			self.state = 'waiting'


	def StopFishBot(self):
		self.state = 'stop'
		player.SetAttackKeyState(TRUE)
		player.SetAttackKeyState(FALSE)
		self.StartFishBotx = XX()
		self.StartFishBotx.XX1(float(99999999999))
		self.StartFishBotx.XX2(self.StartFishBotg)

	def UseBait(self):
		for Slot in xrange(player.INVENTORY_PAGE_SIZE * 5):
			if player.GetItemIndex(Slot) in (27800, 27801, 27802):
				net.SendItemUsePacket(Slot)
				break

	def AddBait(self):
		Bait = player.GetItemCountByVnum
		if Bait(27802) == 0 and Bait(27801) == 0 and Bait(27800) == 0:
			self.state = 'stop'
			return 0

		self.UseBait()
		return 1


	def BubbleAppear(self):
		if chrmgr.IsPossibleEmoticon(-1) == 1:
			return 0
		else:
			return 1

	def RandomTolerance(self):
		Tolerance = float(10)
		Rnd = app.GetRandom(0, int(Tolerance))
		return DivideToFloat1(Rnd, 10)


	def OpenWindowCzytajnik(self):
		if self.BoardCzyelnika.IsShow():
			self.BoardCzyelnika.Hide()
		else:
			self.BoardCzyelnika.Show()

	def CloseCzytajnik(self):
		self.BoardCzyelnika.Hide()


	def OpenWindowZap(self):
		if self.BoardZap.IsShow():
			self.BoardZap.Hide()
		else:
			self.BoardZap.Show()

	def CloseZap(self):
		self.BoardZap.Hide()

	def OpenWindowBossbok(self):
		if self.BoardBoss.IsShow():
			self.BoardBoss.Hide()
		else:
			self.BoardBoss.Show()

	def CloseBossOkno(self):
		self.BoardBoss.Hide()

	def OpenWindowMetinbok(self):
		if self.BoardMetin.IsShow():
			self.BoardMetin.Hide()
		else:
			self.BoardMetin.Show()

	def OpenWindowLow(self):
		if self.BoardLow.IsShow():
			self.BoardLow.Hide()
		else:
			self.BoardLow.Show()

	def CloseLow(self):
		self.BoardLow.Hide()

	def OpenWindowInfoLow(self):
		if self.BoardLow1.IsShow():
			self.BoardLow1.Hide()
		else:
			self.BoardLow1.Show()
	def CloseLowInfo(self):
		self.BoardLow1.Hide()

	def CloseMetinOkno(self):
		self.BoardMetin.Hide()

	def OpenWindowShopScanner(self):
		if self.ShopScannerBoard.IsShow():
			self.ShopScannerBoard.Hide()
		else:
			self.ShopScannerBoard.Show()

	def OpenWindow(self):
		global SPAM
		self.btns3.Hide()
		SPAM = TRUE
		if self.Board1.IsShow():
			self.Board1.Hide()
		else:
			self.Board1.Show()

	def OpenWindowPickup(self):
		if self.BoardPickup.IsShow():
			self.BoardPickup.Hide()
		else:
			self.BoardPickup.Show()

	def OpenWindowKopacz(self):
		if self.BoardKopacz.IsShow():
			self.BoardKopacz.Hide()
		else:
			self.BoardKopacz.Show()

	def OpenWindowPickupInfo(self):
		if self.BoardPickupInfo.IsShow():
			self.BoardPickupInfo.Hide()
		else:
			self.BoardPickupInfo.Show()

	def OpenWindowWykr(self):
		if self.WykrywaczOkno.IsShow():
			self.WykrywaczOkno.Hide()
		else:
			self.WykrywaczOkno.Show()

	def OpenWindowDopy(self):
		if self.DopalaczeOknoBoard.IsShow():
			self.DopalaczeOknoBoard.Hide()
		else:
			self.DopalaczeOknoBoard.Show()
	def OpenWindowSpam(self):
		if self.Spambotboard.IsShow():
			self.Spambotboard.Hide()
		else:
			self.Spambotboard.Show()

	def OpenWindowUstawieniao(self):
		if self.Ustawieniao.IsShow():
			self.Ustawieniao.Hide()
		else:
			self.Ustawieniao.Show()

	def OpenWindowOtwieraczBoard(self):
		if self.OtwieraczBoard.IsShow():
			self.OtwieraczBoard.Hide()
		else:
			self.OtwieraczBoard.Show()

	def OpenWindowUlepsz(self):
		if self.UlepszBoard.IsShow():
			self.UlepszBoard.Hide()
		else:
			self.UlepszBoard.Show()

	def OpenWindowPogoda(self):
		if self.Pogoda.IsShow():
			self.Pogoda.Hide()
		else:
			self.Pogoda.Show()


	def AutoSkileWindow(self):
		self.Aurax.Hide()
		self.Berekx.Hide()
		self.Silnex.Hide()
		self.Ostrzex.Hide()
		self.Strachx.Hide()
		self.Zbrojax.Hide()
		self.Ochronkax.Hide()
		self.Duchx.Hide()
		self.Pomocx.Hide()
		self.Odbiciex.Hide()
		self.Blogox.Hide()
		self.Zwinnoscx.Hide()
		self.Atakx.Hide()
		self.Aurax1.Hide()
		self.Berekx1.Hide()
		self.Silnex1.Hide()
		self.Ostrzex1.Hide()
		self.Strachx1.Hide()
		self.Zbrojax1.Hide()
		self.Ochronkax1.Hide()
		self.Duchx1.Hide()
		self.Pomocx1.Hide()
		self.Blogox1.Hide()
		self.Odbiciex1.Hide()
		self.Zwinnoscx1.Hide()
		self.Atakx1.Hide()

		self.slotbar_Skill1czas.Hide()
		self.slotbar_Skill2czas.Hide()
		self.slotbar_Skill3czas.Hide()
		if self.AutoSkileBoard.IsShow():
			self.AutoSkileBoard.Hide()
		else:
			self.AutoSkileBoard.Show()
		Race = net.GetMainActorRace()
		Group = net.GetMainActorSkillGroup()
		if (Race == 0 and Group == 1) or (Race == 4 and Group == 1):
			self.Aurax.Show()
			self.Berekx.Show()
			self.Aurax1.Show()
			self.Berekx1.Show()
			self.slotbar_Skill1czas.Show()
			self.slotbar_Skill2czas.Show()
			self.AutoSkileBoard.SetSize(112, 110)
		if (Race == 0 and Group == 2) or (Race == 4 and Group == 2):
			self.Silnex.Show()
			self.Silnex1.Show()
			self.slotbar_Skill1czas.Show()
			self.AutoSkileBoard.SetSize(72, 110)
		if (Race == 2 and Group == 1) or (Race == 6 and Group == 1):
			self.Ostrzex.Show()
			self.Strachx.Show()
			self.Zbrojax.Show()
			self.Ostrzex1.Show()
			self.Strachx1.Show()
			self.Zbrojax1.Show()
			self.slotbar_Skill1czas.Show()
			self.slotbar_Skill2czas.Show()
			self.slotbar_Skill3czas.Show()
			self.AutoSkileBoard.SetSize(152, 110)
		if (Race == 2 and Group == 2) or (Race == 6 and Group == 2):
			self.Ochronkax.Show()
			self.Duchx.Show()
			self.Ochronkax1.Show()
			self.Duchx1.Show()
			self.slotbar_Skill1czas.Show()
			self.slotbar_Skill2czas.Show()
			self.AutoSkileBoard.SetSize(112, 110)
		if (Race == 3 and Group == 1) or (Race == 7 and Group == 1):
			self.Blogox.Show()
			self.Odbiciex.Show()
			self.Pomocx.Show()
			self.Blogox1.Show()
			self.Odbiciex1.Show()
			self.Pomocx1.Show()
			self.slotbar_Skill1czas.Show()
			self.slotbar_Skill2czas.Show()
			self.slotbar_Skill3czas.Show()
			self.AutoSkileBoard.SetSize(152, 110)
		if (Race == 3 and Group == 2) or (Race == 7 and Group == 2):
			self.Zwinnoscx.Show()
			self.Atakx.Show()
			self.Zwinnoscx1.Show()
			self.Atakx1.Show()
			self.slotbar_Skill1czas.Show()
			self.slotbar_Skill3czas.Show()
			self.slotbar_Skill3czas.SetPosition(63, 75)
			self.AutoSkileBoard.SetSize(112, 110)

	def OpenWindowInfo(self):
		if self.BoardInfo.IsShow():
			self.BoardInfo.Hide()
		else:
			self.BoardInfo.Show()

	def OpenWindowStatusPlus(self):
		if self.BoardStatusPlus.IsShow():
			self.BoardStatusPlus.Hide()
		else:
			self.BoardStatusPlus.Show()

	def OpenWindowInfoKopacz(self):
		if self.BoardInfoKopacz.IsShow():
			self.BoardInfoKopacz.Hide()
		else:
			self.BoardInfoKopacz.Show()

	def OpenWindowInfoBossy(self):
		if self.BoardInfoBossy.IsShow():
			self.BoardInfoBossy.Hide()
		else:
			self.BoardInfoBossy.Show()

	def OpenWindowAutoMetin(self):
		if self.BoardAutoMetin.IsShow():
			self.BoardAutoMetin.Hide()
		else:
			self.BoardAutoMetin.Show()

	def OpenWindowBuffbot(self):
		if self.BoardBuffbot.IsShow():
			self.BoardBuffbot.Hide()
		else:
			self.BoardBuffbot.Show()

	def OpenWindowRozdzielanie(self):
		if self.BoardRozdzielanie.IsShow():
			self.BoardRozdzielanie.Hide()
		else:
			self.BoardRozdzielanie.Show()

	def OpenWindowGildia(self):
		if self.BoardGildia.IsShow():
			self.BoardGildia.Hide()
		else:
			self.BoardGildia.Show()

	def OpenWindowNew(self):
		if self.BoardNew.IsShow():
			self.BoardNew.Hide()
		else:
			self.BoardNew.Show()

	def CloseNew(self):
		self.BoardNew.Hide()
	def Close(self):
		global SPAM
		self.Board1.Hide()
		self.btns3.Show()
		SPAM = FALSE

	def CloseKopacz(self):
		self.BoardKopacz.Hide()

	def CloseStatusPlus(self):
		self.BoardStatusPlus.Hide()

	def CloseWykr(self):
		self.WykrywaczOkno.Hide()

	def CloseDopy(self):
		self.DopalaczeOknoBoard.Hide()

	def Spambotclose(self):
		self.Spambotboard.Hide()

	def Ustawieniaoclose(self):
		self.Ustawieniao.Hide()

	def OtwieraczBoardclose(self):
		self.OtwieraczBoard.Hide()

	def Typstrclose(self):
		self.Typstr.Hide()

	def CloseUlepsz(self):
		self.UlepszBoard.Hide()

	def ClosePogoda(self):
		self.Pogoda.Hide()

	def AutoSkileClose(self):
		self.AutoSkileBoard.Hide()

	def ClosePickup(self):
		self.BoardPickup.Hide()

	def ClosePickupInfo(self):
		self.BoardPickupInfo.Hide()

	def CloseInfo(self):
		self.BoardInfo.Hide()

	def CloseInfoKopacz(self):
		self.BoardInfoKopacz.Hide()

	def CloseInfoBossy(self):
		self.BoardInfoBossy.Hide()

	def CloseAutoMetin(self):
		self.BoardAutoMetin.Hide()

	def CloseRozdzielanie(self):
		self.BoardRozdzielanie.Hide()

	def CloseGildia(self):
		self.BoardGildia.Hide()


	def CloseShopScanner(self):
		self.ShopScannerBoard.Hide()

	def CloseBuffbot(self):
		self.BoardBuffbot.Hide()



class XX(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def XX1(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Show()

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def XX2(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)


	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()

		else:
			return

class ExampleBoard(ui.ScriptWindow):
	def __init__(self, parent, x, y):
		ui.ScriptWindow.__init__(self)
		self.ShopScannerBoard = self.CreateBoard(parent, 350, 50, x, y)
		self.gui = {
				'buttons' : {
					'Podglad' : self.CreateButton(self.ShopScannerBoard, 10 + 50 * 0, 10 + 25 * 0, 'Podglad',self.Podglad),
					'TP' : self.CreateButton(self.ShopScannerBoard, 10 + 50 * 0, 10 + 25 * 1, 'TP',self.Teleport),
					},
				'textlines' : {
					'cena': self.CreateTextline(self.ShopScannerBoard, 85, 35),
					'ilosc': self.CreateTextline(self.ShopScannerBoard, 240, 35),
					'Nazwa': self.CreateTextline(self.ShopScannerBoard, 85, 10),
					},
				}
	def Podglad(self):
		global listaWysz
		net.SendOnClickPacket(listaWysz[self.index][4])
	def Teleport(self):
		global listaWysz
		(XS, YS, ZS) = chr.GetPixelPosition(listaWysz[self.index][4])
		self.TeleportToDest(XS,YS)
	def DivideToFloat(self,x, y):
		try:
			return x * (y**-1)
		except:
			return 0
	def GetTmpTeleport(self,DestX, DestY):
		global DivideToFloat
		(PlayerX, PlayerY, PlayerZ) = player.GetMainCharacterPosition()
		DifX = DestX - PlayerX
		DifY = DestY - PlayerY
		Vektor = self.DivideToFloat(2000, math.sqrt(DifX**2 + DifY**2))
		TempX = PlayerX + Vektor*DifX
		TempY = PlayerY + Vektor*DifY
		Count = self.DivideToFloat((DestX - PlayerX), (Vektor*DifX))
		return (TempX, TempY, Count)
	def Debug(self):
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
	def TeleportToDest(self,aimx, aimy):
		global Debug, GetTmpTeleport, TeleportState
		(TmpX, TmpY, Count) = self.GetTmpTeleport(aimx, aimy)
		TmpCount = 0
		myVid = player.GetMainCharacterIndex()
		while TmpCount < Count:
			chr.SelectInstance(myVid)
			(TmpX, TmpY, Crap) = self.GetTmpTeleport(aimx, aimy)
			chr.SetPixelPosition(int(TmpX), int(TmpY))
			TmpCount += 1
			self.Debug()
		chr.SetPixelPosition(int(aimx), int(aimy))
		self.Debug()
		TeleportState = 1
		chr.SelectInstance(myVid)
	def SetBoardInfo(self, index, price, amount, nazwa):
		self.index = index
		self.gui['textlines']['cena'].SetText('Cena: %s Yang' % price)
		self.gui['textlines']['ilosc'].SetText('Ilosc: %s' % amount)
		self.gui['textlines']['Nazwa'].SetText('Nazwa: %s' % nazwa)
	def GetIndex(self):
		return self.index
	def HideBoard(self):
		self.board.Hide()
	def ShowBoard(self):
		self.board.Show()
	def CreateTextline(self, parent, x, y):
		textline = ui.TextLine()
		textline.SetParent(parent)
		textline.SetPosition(x,y)
		textline.Show()
		return textline
	def CreateBoard(self, parent, width, height, x, y):
		board = ui.Board()
		board.SetParent(parent)
		board.SetSize(width, height)
		board.SetPosition(x, y)
		board.SetTop()
		board.Show()
		return board
	def CreateButton(self, parent, x, y, text, event):
		button = ui.Button()
		button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual('d:/ymir work/ui/public/Middle_Button_01.sub')
		button.SetOverVisual('d:/ymir work/ui/public/Middle_Button_02.sub')
		button.SetDownVisual('d:/ymir work/ui/public/Middle_Button_03.sub')
		button.SetText(text)
		button.SetEvent(event)
		button.Show()
		return button
	def __del__(self):
		ui.ScriptWindow.__del__(self)
	def Destroy(self):
		self.Hide()


class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
		button = ui.ToggleButton()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetToggleUpEvent(funcUp)
		button.SetToggleDownEvent(funcDown)
		return button


	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(5, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value

	def TextLine(self, parent, textlineText, x, y, color,rozmiar):
		textline = ui.TextLine()
		textline.SetFontName(rozmiar)
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline

	def SlotbarText(self, parent, editlineText, x, y, width, heigh):
		SlotBar = ui.SlotBar()
		SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		TextLine = ui.TextLine()
		TextLine.SetParent(SlotBar)
		TextLine.SetText(editlineText)
		TextLine.SetHorizontalAlignCenter()
		TextLine.SetVerticalAlignCenter()
		TextLine.SetWindowHorizontalAlignCenter()
		TextLine.SetWindowVerticalAlignCenter()
		TextLine.Show()
		return SlotBar, TextLine


	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

	def SliderBar(self, parent, sliderPos, func, x, y):
		Slider = ui.SliderBar()
		if parent != None:
			Slider.SetParent(parent)
		Slider.SetPosition(x, y)
		Slider.SetSliderPos(sliderPos / 100)
		Slider.Show()
		Slider.SetEvent(func)
		return Slider

	def ExpandedImage(self, parent, x, y, img):
		image = ui.ExpandedImageBox()
		if parent != None:
			image.SetParent(parent)
		image.SetPosition(x, y)
		image.LoadImage(img)
		image.Show()
		return image

	def ComboBox(self, parent, text, x, y, width):
		combo = ui.ComboBox()
		if parent != None:
			combo.SetParent(parent)
		combo.SetPosition(x, y)
		combo.SetSize(width, 15)
		combo.SetCurrentItem(text)
		combo.Show()
		return combo

	def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
		thin = ui.ThinBoard()
		if parent != None:
			thin.SetParent(parent)
		if moveable == TRUE:
			thin.AddFlag('movable')
			thin.AddFlag('float')
		thin.SetSize(width, heigh)
		thin.SetPosition(x, y)
		if center == TRUE:
			thin.SetCenterPosition()
		thin.Show()
		return thin

	def Gauge(self, parent, width, color, x, y):
		gauge = ui.Gauge()
		if parent != None:
			gauge.SetParent(parent)
		gauge.SetPosition(x, y)
		gauge.MakeGauge(width, color)
		gauge.Show()
		return gauge

	def ListBoxEx(self, parent, x, y, width, heigh, SVIC, event):
		bar = ui.Bar()
		if parent != None:
			bar.SetParent(parent)
		bar.SetPosition(x, y)
		bar.SetSize(width, heigh)
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.SetViewItemCount(SVIC)
		ListBox.SetSelectEvent(event)
		ListBox.Show()
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox

	def ListBoxEx1(self, parent, x, y, width, heigh, SVIC, event):
		bar = ui.Bar()
		if parent != None:
			bar.SetParent(parent)
		bar.SetPosition(x, y)
		bar.SetSize(width, heigh)
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.SetViewItemCount(SVIC)
		ListBox.SetSelectEvent(event)
		ListBox.Show()
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox

	def HorizontalBar(self, parent, x, y, Create):
		horizontalBar = ui.HorizontalBar()
		if parent != None:
			horizontalBar.SetParent(parent)
		horizontalBar.SetPosition(x, y)
		horizontalBar.Create(Create)
		horizontalBar.Show()
		return horizontalBar

	def GetCurrentText(self):
		return self.textLine.GetText()
	def OnSelectItem(self, index, name):
		self.SetCurrentItem(name)
		self.CloseListBox()
		self.event()
	ui.ComboBox.GetCurrentText = GetCurrentText
	ui.ComboBox.OnSelectItem = OnSelectItem

class Item(ui.ListBoxEx.Item):
	def __init__(self, text):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=text
		self.textLine=self.__CreateTextLine(text[:1000])
	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)
	def GetText(self):
		return self.text
	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self,2*len(self.textLine.GetText()) + 35, height)
	def __CreateTextLine(self, text):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		textLine.SetText(text)
		textLine.Show()
		return textLine
Dialog1().Show()
#wszystko0=d0+d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11+d12+d13+d14+d15+d16+d17+d18+d19+d20+d21+d22+d23+d24+d25+d26+d27+d28+d29+d30+d31+d32+d33+d34+d35+d36+d37+d38+d39+d40+d41+d42+d43+d44+d45+d46+d47+d48+d49+d50+d51+d52+d53+d54+d55+d56+d57+d58+d59+d60+d61+d62+d63+d64+d65+d66+d67+d68+d69+d70+d71+d72+d73+d74+d75+d76+d77+d78+d79+d80+d81+d82+d83+d84+d85+d86+d87+d88+d89+d90+d91+d92+d93+d94+d95+d96+d97+d98+d99+d100+d101+d102+d103+d104+d105+d106+d107+d108+d109+d110+d111+d112+d113+d114+d115+d116+d117+d118+d119+d120+d121+d122+d123+d124+d125+d126+d127+d128+d129+d130+d131+d132+d133+d134+d135+d136+d137+d138+d139+d140+d141+d142+d143+d144+d145+d146+d147+d148+d149+d150+d151+d152+d153+d154+d155+d156+d157+d158+d159+d160+d161+d162+d163+d164+d165+d166+d167+d168+d169+d170+d171+d172+d173+d174+d175+d176+d177+d178+d179+d180+d181+d182+d183+d184+d185+d186+d187+d188+d189+d190+d191+d192+d193+d194+d195+d196+d197+d198+d199+d200+d201+d202+d203+d204+d205+d206+d207+d208+d209+d210+d211+d212+d213+d214+d215+d216+d217+d218+d219+d220+d221+d222+d223+d22
#wszystko1=d2210+d2211+d2212+d2213+d2214+d2215+d2216+d2217+d2218+d2219+d2220+d2221+d2222+d2223+d2224+d2225+d2226+d2227+d2228+d2229+d2230+d2231+d2232+d2233+d2234+d2235+d2236+d2237+d2238+d2239+d2240+d2241+d2242+d2243+d2244+d2245+d2246+d2247+d2248+d2249+d2250+d2251+d2252+d2253+d2254+d2255+d2256+d2257+d2258+d2259+d2260+d2261+d2262+d2263+d2264+d2265+d2266+d2267+d2268+d2269+d2270+d2271+d2272+d2273+d2274+d2275+d2276+d2277+d2278+d2279+d2280+d2281+d2282+d2283+d2284+d2285+d2286+d2287+d2288+d2289+d2290+d2291+d2292+d2293+d2294+d2295+d2296+d2297+d2298+d2299+d2300+d2301+d2302+d2303+d2304+d2305+d2306+d2307+d2308+d2309+d2310+d2311+d2312+d2313+d2314+d2315+d2316+d2317+d2318+d2319+d2320+d2321+d2322+d2323+d2324+d2325+d2326+d2327+d2328+d2329+d2330+d2331+d2332+d2333+d2334+d2335+d2336+d2337+d2338+d2339+d2340+d2341+d2342+d2343+d2344+d2345+d2346+d2347+d2348+d2349+d2350+d2351+d2352+d2353+d2354+d2355+d2356+d2357+d2358+d2359+d2360+d2361+d2362+d2363+d2364+d2365+d2366+d2367+d2368+d2369+d2370+d2371+d2372+d2373+d2374+d2375+d2376+d2377+d2378
#wszystko=wszystko0+wszystko1
#exec(wszystko)
