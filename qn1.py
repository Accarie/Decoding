from aspose.barcode import barcoderecognition

reader = barcoderecognition.BarCodeReader("image01.jpg", barcoderecognition.DecodeType.ALL_SUPPORTED_TYPES)
recognized_results = reader.read_bar_codes()
for barcode in recognized_results:
    print(barcode.code_text)