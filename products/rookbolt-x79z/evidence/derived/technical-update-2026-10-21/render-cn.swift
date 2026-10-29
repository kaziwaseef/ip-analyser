import Foundation
import PDFKit
import AppKit

let args = CommandLine.arguments
let document = PDFDocument(url: URL(fileURLWithPath: args[1]))!
let output = URL(fileURLWithPath: args[2])
for pageNumber in [2, 5, 10] {
    let page = document.page(at: pageNumber - 1)!
    let box = page.bounds(for: .mediaBox)
    let size = NSSize(width: box.width * 1.6, height: box.height * 1.6)
    let image = page.thumbnail(of: size, for: .mediaBox)
    let bitmap = NSBitmapImageRep(data: image.tiffRepresentation!)!
    try! bitmap.representation(using: .png, properties: [:])!.write(to: output.appendingPathComponent("CN222884700U-page-\(pageNumber).png"))
}
print("Rendered original CN claims, detailed embodiment and exploded figure pages")
