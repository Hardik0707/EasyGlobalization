
import wx
import EasyGlobalization as i19n

class Main ( wx.Frame ):
	
	
	def __init__( self, parent ):

		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"EasyGlobalization v1.0", pos = wx.DefaultPosition, size = wx.Size( 350,400 ), style = (wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX)|wx.CAPTION| wx.MINIMIZE_BOX|wx.CLOSE_BOX )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetIcon(wx.Icon("logo.png"))
		
		MainLayout = wx.BoxSizer( wx.VERTICAL )
		
		#Option Section
		Options = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.VERTICAL )

		ParamSelectors = wx.GridSizer( 3, 2, 0, 0 )

		#Select Framework 
		self.SelectFramework = wx.StaticText( Options.GetStaticBox(), wx.ID_ANY, u"Select Framework : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SelectFramework.Wrap( -1 )
		self.SelectFramework.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		self.SelectFramework.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		ParamSelectors.Add( self.SelectFramework, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		SelectFrameworkChoice = i19n.SelectFramework()
		self.SFChoice = wx.Choice( Options.GetStaticBox(), wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 150,-1 ), SelectFrameworkChoice, wx.CB_SORT )
		self.SFChoice.SetSelection( 0 )
		self.SFChoice.SetExtraStyle( wx.WS_EX_BLOCK_EVENTS )
		self.SFChoice.SetToolTip( u"Select Framework" )
		#Base Language
		ParamSelectors.Add( self.SFChoice, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		 
		self.BaseLanguage = wx.StaticText( Options.GetStaticBox(), wx.ID_ANY, u"Base Language : ", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.BaseLanguage.Wrap( -1 )
		self.BaseLanguage.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		self.BaseLanguage.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		ParamSelectors.Add( self.BaseLanguage, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		BaseLanguageChoice = i19n.SelectBaseLanguage()
		self.BLChoice = wx.Choice( Options.GetStaticBox(), wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 150,-1 ), BaseLanguageChoice, wx.CB_SORT )
		self.BLChoice.SetSelection( 0 )
		self.BLChoice.SetExtraStyle( wx.WS_EX_BLOCK_EVENTS )
		self.BLChoice.SetToolTip( u"Select Base Language" )
		
		#Destination Language 
		ParamSelectors.Add( self.BLChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.DestinationLanguage = wx.StaticText( Options.GetStaticBox(), wx.ID_ANY, u"Destination Language : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DestinationLanguage.Wrap( -1 )
		self.DestinationLanguage.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		self.DestinationLanguage.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		ParamSelectors.Add( self.DestinationLanguage, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		DestinationLanguageChoice = i19n.SelectDestinationLanguage()
		self.DLChoice = wx.Choice( Options.GetStaticBox(), wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 150,-1 ), DestinationLanguageChoice, wx.CB_SORT )
		self.DLChoice.SetSelection(1)
		self.DLChoice.SetExtraStyle( wx.WS_EX_BLOCK_EVENTS )
		self.DLChoice.SetToolTip( u"Select Destination Language" )
		
		ParamSelectors.Add( self.DLChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
	
		Options.Add( ParamSelectors, 1, wx.EXPAND, 5 )

		MainLayout.Add( Options, 1, wx.EXPAND, 5 )
		
		#Static LIne
		self.StaticLine1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.StaticLine1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		#Source File Section
		MainLayout.Add( self.StaticLine1, 0, wx.EXPAND |wx.ALL, 5 )
		
		SourcesOption = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Source File" ), wx.VERTICAL )
		
		FileSelectors = wx.GridSizer( 1, 3, 0, 0 )
		
		self.STFileSelect = wx.StaticText( SourcesOption.GetStaticBox(), wx.ID_ANY, u"Selected File : ", wx.Point( -1,-1 ), wx.DefaultSize, wx.ALIGN_CENTRE )
		self.STFileSelect.Wrap( -1 )
		self.STFileSelect.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		self.STFileSelect.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		FileSelectors.Add( self.STFileSelect, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SelectedFile = wx.TextCtrl( SourcesOption.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.SelectedFile.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		FileSelectors.Add( self.SelectedFile, 0, wx.ALL, 5 )
		
		self.BrowserFile = wx.Button( SourcesOption.GetStaticBox(), wx.ID_ANY, u"Browse...", wx.DefaultPosition, wx.DefaultSize, 0 )
		FileSelectors.Add( self.BrowserFile, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		SourcesOption.Add( FileSelectors, 1, wx.EXPAND, 5 )
		
		MainLayout.Add( SourcesOption, 1, wx.EXPAND, 5 )
		
		#Static Line
		self.StaticLine1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		MainLayout.Add( self.StaticLine1, 0, wx.EXPAND |wx.ALL, 5 )
		
		Destination = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Generated File Details" ), wx.VERTICAL )
		
		DestFileSelector = wx.GridSizer( 2, 2, 0, 0 )
		
		self.STDestFileNameLabel = wx.StaticText( Destination.GetStaticBox(), wx.ID_ANY, u"File Name : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.STDestFileNameLabel.Wrap( -1 )
		self.STDestFileNameLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		#Selected File Name
		DestFileSelector.Add( self.STDestFileNameLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.TCDestFileName = wx.TextCtrl( Destination.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.TCDestFileName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		#Selected File Path
		DestFileSelector.Add( self.TCDestFileName, 0, wx.ALL, 5 )
		
		self.STDestFilePathLabel = wx.StaticText( Destination.GetStaticBox(), wx.ID_ANY, u"File Path : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.STDestFilePathLabel.Wrap( -1 )
		self.STDestFilePathLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		DestFileSelector.Add( self.STDestFilePathLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.TCDestFilePath = wx.TextCtrl( Destination.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.TCDestFilePath.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		DestFileSelector.Add( self.TCDestFilePath, 0, wx.ALL, 5 )
		
		Destination.Add( DestFileSelector, 1, wx.EXPAND, 5 )
		
		MainLayout.Add( Destination, 1, wx.EXPAND, 5 )
		#Static Line
		self.StaticLine2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		MainLayout.Add( self.StaticLine2, 0, wx.EXPAND |wx.ALL, 5 )
		
		#Generate Button
		self.GenerateButton = wx.Button( self, wx.ID_ANY, u"Generate File", wx.DefaultPosition, wx.DefaultSize, 0 )
		MainLayout.Add( self.GenerateButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		# Menu Bar
		self.SetSizer( MainLayout )
		self.Layout()
		self.MenuBar = wx.MenuBar( 0 )
		self.MenuBar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.MenuBar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.FileMenu = wx.Menu()
		self.FileSelectFile = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Select Resource File"+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileMenu.Append( self.FileSelectFile )
		
		self.FileGenerate = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Generate"+ u"\t" + u"F5", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileMenu.Append( self.FileGenerate )
		self.FileGenerate.Enable( False )
		
		self.FileMenu.AppendSeparator()
		
		self.FileExit = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Exit"+ u"\t" + u"Alt+F4", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileMenu.Append( self.FileExit )
		
		self.MenuBar.Append( self.FileMenu, u"File" ) 
		
		self.HelpMenu = wx.Menu()
		self.HelpDocumentation = wx.MenuItem( self.HelpMenu, wx.ID_ANY, u"Online Documentation"+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.HelpMenu.Append( self.HelpDocumentation )
		
		self.HelpViewSourceCode = wx.MenuItem( self.HelpMenu, wx.ID_ANY, u"View Source Code"+ u"\t" + u"F2", wx.EmptyString, wx.ITEM_NORMAL )
		self.HelpMenu.Append( self.HelpViewSourceCode )

		self.MenuBar.Append( self.HelpMenu, u"Help" ) 
		self.SetMenuBar( self.MenuBar )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.BrowserFile.Bind( wx.EVT_BUTTON, self.BrowserFileOnButtonClick )
		self.GenerateButton.Bind( wx.EVT_BUTTON, self.GenerateButtonOnButtonClick )
		self.Bind( wx.EVT_MENU, self.FileGenerateOnMenuSelection, id = self.FileGenerate.GetId() )
		self.Bind( wx.EVT_MENU, self.FileExitOnMenuSelection, id = self.FileExit.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def BrowserFileOnButtonClick( self, event ):
		openFileDialog = wx.FileDialog(frame, "Open", "", "", "Resource files (*.resx)|*.resx", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		openFileDialog.ShowModal()
		
		self.SelectedFile.Value=openFileDialog.GetPath()
		self.TCDestFileName.Value,self.TCDestFilePath.Value = i19n.GenerateNewFileDetails(openFileDialog.GetPath(),self.DLChoice.GetStringSelection())
		
		# print(self.TCDestFileName.Value,self.TCDestFilePath.GetValue())
		openFileDialog.Destroy()
	
	def GenerateButtonOnButtonClick( self, event ):
		Newfilepath = self.TCDestFilePath.GetValue()+self.TCDestFileName.GetValue()
		try:
			xmltree = i19n.GenerateTranslatedFile(filepath=self.SelectedFile.Value,base_lang=self.BLChoice.GetStringSelection(),dest_lang=self.DLChoice.GetStringSelection())
			xmltree.write(Newfilepath,encoding='utf-8',method='xml',xml_declaration=True)
			wx.MessageBox('File Generated Successfully !\nLocation: '+Newfilepath, ' Success', wx.OK | wx.ICON_INFORMATION)
		except:
			wx.MessageBox('ERROR: Failed to Generate File.', ' Error', wx.OK | wx.ICON_ERROR)
	
	def FileGenerateOnMenuSelection( self, event ):
		event.Skip()
	
	def FileExitOnMenuSelection( self, event ):
		self.Destroy()
		# event.Skip()

app = wx.App()
frame = Main(None)
frame.Show()
app.MainLoop()
del app
