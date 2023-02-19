from Position import CalculationPosition
from KompasTools import KompasTools
from FilePath import Path

def main():
	ObjectsPath = Path()
	PathSave = ObjectsPath.path_window()
	ObjectsKompasTools = KompasTools(PathSave)
	DataPatterns = ObjectsPath.read_json()
	ObjectsKompasTools.create_doc()
	ObjectsKompasTools.layers()
	Number = 0
	StepX = 0
	for Pattern in DataPatterns:
		ObjectsCalculationPosition = CalculationPosition(Pattern["Length"], Pattern["Width"], Pattern["Angle"])
		CoordinatesContour = ObjectsCalculationPosition.define_сoordinates_contour()
		# Text = Pattern["Name"]
		SizesText = ObjectsCalculationPosition.get_text_metrics(22)
		CoordinatesText = ObjectsCalculationPosition.define_сoordinates_text()
		ObjectsKompasTools.set_parameters(	Pattern, 
											CoordinatesContour, 
											SizesText, 
											CoordinatesText,
											(StepX, 0))
		ObjectsKompasTools.iDocument2D.ksLayer(1)
		ObjectsKompasTools.create_contour_pattern()
		ObjectsKompasTools.iDocument2D.ksLayer(2)
		ObjectsKompasTools.create_text_pattern()
		ObjectsKompasTools.iDocument2D.ksLayer(0)
		StepX += 500
		Number+=1
	ObjectsKompasTools.save_doc('Схема выкроек')
	ObjectsKompasTools.close_doc()

if __name__ == "__main__":
	main()