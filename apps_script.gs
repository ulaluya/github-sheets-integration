function doPost(e) {
  var data = JSON.parse(e.postData.contents);
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.clear();
  sheet.appendRow(["SHA", "Author", "Message", "Date"]);
  for (var i = 0; i < data.length; i++) {
    sheet.appendRow([
      data[i].sha,
      data[i].author,
      data[i].message,
      data[i].date
    ]);
  }
  return ContentService.createTextOutput("Success").setMimeType(ContentService.MimeType.TEXT);
}