f = open('helloworld.html','w')

message = """<html>
<head></head>
<style>
table { border-collapse: collapse; font-family: Calibri, sans-serif; }
colgroup, tbody { border: solid medium; }
td { border: solid thin; height: 1.4em; width: 1.4em; text-align: center; padding: 0; }
</style>
<table>
  <caption>Sudoku of the day</caption>
  <colgroup><col><col><col>
  <colgroup><col><col><col>
  <colgroup><col><col><col>
  <tbody>
   <tr> <td>1 <td>  <td>3 <td>6 <td>  <td>4 <td>7 <td>  <td>9
   <tr> <td>  <td>2 <td>  <td>  <td>9 <td>  <td>  <td>1 <td>
   <tr> <td>7 <td>  <td>  <td>  <td>  <td>  <td>  <td>  <td>6
  <tbody>
   <tr> <td>2 <td>  <td>4 <td>  <td>3 <td>  <td>9 <td>  <td>8
   <tr> <td>  <td>  <td>  <td>  <td>  <td>  <td>  <td>  <td>
   <tr> <td>5 <td>  <td>  <td>9 <td>  <td>7 <td>  <td>  <td>1
  <tbody>
   <tr> <td>6 <td>  <td>  <td>  <td>5 <td>  <td>  <td>  <td>2
   <tr> <td>  <td>  <td>  <td>  <td>7 <td>  <td>  <td>  <td>
   <tr> <td>9 <td>  <td>  <td>8 <td>  <td>2 <td>  <td>  <td>5
</table>
</html>"""

f.write(message)
f.close()