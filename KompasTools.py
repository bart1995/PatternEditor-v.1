from win32com.client import Dispatch, gencache
import LDefin2D
import MiscellaneousHelpers as MH

class KompasTools:
	def __init__(self, PathSave):
		self.PathSave = PathSave
		self.kompas6_api5_module = gencache.EnsureModule('{0422828C-F174-495E-AC5D-D31014DBBE87}', 0, 1, 0)
		self.kompas_api7_module = gencache.EnsureModule('{69AC2981-37C0-4379-84FD-5DD2F3C0A520}', 0, 1, 0)
		self.kompas6_constants = gencache.EnsureModule('{75C9F5D0-B5B8-4526-8681-9903C567D2ED}', 0, 1, 0).constants
		self.kompas6_constants_3d = gencache.EnsureModule('{2CAF168C-7961-4B90-9DA2-701419BEEFE3}', 0, 1, 0).constants
		self.kompas_object = Dispatch('Kompas.Application.5', None, self.kompas6_api5_module.KompasObject.CLSID)
		self.application = Dispatch('Kompas.Application.7') # или KompasObject.ksGetApplication7()
		self.Documents = self.application.Documents
		self.MyObjects = []
		self.MyObjectsText = []

	def set_parameters(self, PatternParameters, CoordinatesContour, SizesText, CoordinatesText, Step = (0, 0)):
		self.NameProject = PatternParameters["NameProject"]
		self.Name = PatternParameters["Name"]
		self.Angle = PatternParameters["Angle"]
		self.Length = PatternParameters["Length"]
		self.Width = PatternParameters["Width"]
		# self.Group = None
		self.x1, self.y1 = CoordinatesContour[0]
		self.x2, self.y2 = CoordinatesContour[1]
		self.x3, self.y3 = CoordinatesContour[2]
		self.x4, self.y4 = CoordinatesContour[3]
		self.point1 = CoordinatesContour[0]
		self.point2 = CoordinatesContour[1]
		self.point3 = CoordinatesContour[2]
		self.point4 = CoordinatesContour[3]
		self.Coordinates = CoordinatesContour
		self.SizeText, self.WithText = SizesText
		self.xText, self.yText = CoordinatesText
		self.xdText = 0
		self.ydText = 0
		self.StepX, self.StepY = Step
		self.TextKompas = self.Name

	def create_doc(self):
		self.kompas_document = self.Documents.AddWithDefaultSettings(self.kompas6_constants.ksDocumentFragment, True)
		self.kompas_document_2d = self.kompas_api7_module.IKompasDocument2D(self.kompas_document)
		self.iDocument2D = self.kompas_object.ActiveDocument2D()

	def layers(self):
		obj = self.iDocument2D.ksLayer(1)
		iLayerParam = self.kompas6_api5_module.ksLayerParam(self.kompas_object.GetParamStruct(self.kompas6_constants.ko_LayerParam))
		iLayerParam.Init()
		iLayerParam.color = 0
		iLayerParam.name = "Contour"
		iLayerParam.state = 0
		self.iDocument2D.ksSetObjParam(obj, iLayerParam, LDefin2D.ALLPARAM)
		self.MyObjects.append(obj)
		obj = self.iDocument2D.ksLayer(2)
		iLayerParam = self.kompas6_api5_module.ksLayerParam(self.kompas_object.GetParamStruct(self.kompas6_constants.ko_LayerParam))
		iLayerParam.Init()
		iLayerParam.color = 0
		iLayerParam.name = "Text"
		iLayerParam.state = 0
		self.iDocument2D.ksSetObjParam(obj, iLayerParam, LDefin2D.ALLPARAM)
		self.MyObjects.append(obj)

	def create_contour_pattern(self):
		iRectangleParam = self.kompas6_api5_module.ksRectangleParam(self.kompas_object.GetParamStruct(self.kompas6_constants.ko_RectangleParam))
		iRectangleParam.Init()
		if -self.Angle > 0:
			iRectangleParam.x = self.x3 + self.StepX
			iRectangleParam.y = self.y3 + self.StepY
		elif -self.Angle < 0:
			iRectangleParam.x = self.x1 + self.StepX
			iRectangleParam.y = self.y1 + self.StepY
		else:
			iRectangleParam.x = self.x4 + self.StepX
			iRectangleParam.y = self.y4 + self.StepY
		iRectangleParam.ang = -self.Angle
		iRectangleParam.height = self.Width
		iRectangleParam.width = self.Length
		iRectangleParam.style = 1
		Contour = self.iDocument2D.ksRectangle(iRectangleParam)

	def create_text_pattern(self):
			iParagraphParam = self.kompas6_api5_module.ksParagraphParam(self.kompas_object.GetParamStruct(self.kompas6_constants.ko_ParagraphParam))
			iParagraphParam.Init()
			iParagraphParam.x = self.xText + self.xdText + self.StepX
			iParagraphParam.y = self.yText + self.ydText + self.StepY
			if self.Angle != 0:
				iParagraphParam.ang = self.Angle
			else:
				iParagraphParam.ang = self.Angle + 90
			iParagraphParam.height = 50
			iParagraphParam.width = 50
			iParagraphParam.hFormat = 0
			iParagraphParam.vFormat = 0
			iParagraphParam.style = 1
			self.iDocument2D.ksParagraph(iParagraphParam)
			iTextLineParam = self.kompas6_api5_module.ksTextLineParam(self.kompas_object.GetParamStruct(self.kompas6_constants.ko_TextLineParam))
			iTextLineParam.Init()
			iTextLineParam.style = 1
			iTextItemArray = self.kompas_object.GetDynamicArray(LDefin2D.TEXT_ITEM_ARR)
			iTextItemParam = self.kompas6_api5_module.ksTextItemParam(self.kompas_object.GetParamStruct(self.kompas6_constants.ko_TextItemParam))
			iTextItemParam.Init()
			iTextItemParam.iSNumb = 0
			iTextItemParam.s = self.TextKompas
			iTextItemParam.type = 0
			iTextItemFont = self.kompas6_api5_module.ksTextItemFont(iTextItemParam.GetItemFont())
			iTextItemFont.Init()
			iTextItemFont.bitVector = 4096
			iTextItemFont.color = 0
			iTextItemFont.fontName = "GOST type A (plotter)"
			iTextItemFont.height = self.SizeText
			iTextItemFont.ksu = 1
			iTextItemArray.ksAddArrayItem(-1, iTextItemParam)
			iTextLineParam.SetTextItemArr(iTextItemArray)
			self.iDocument2D.ksTextLine(iTextLineParam)
			Text = self.iDocument2D.ksEndObj()
			ConvertText = self.iDocument2D.ksConvertTextToCurve(Text)
			GroupText = self.iDocument2D.ksStoreTmpGroup(ConvertText)
			self.xdText = 0
			self.ydText = 0
			self.iDocument2D.ksDeleteObj(Text)

	def save_doc(self, FileName):
		self.kompas_document.SaveAs('{}/{}.dxf'.format(self.PathSave, FileName))

	def close_doc(self):
		self.kompas_document.Close(False)

	def delete_objects(self):
		for MyObject in self.MyObjects:
			self.iDocument2D.ksDeleteObj(MyObject)
		self.MyObjects = []