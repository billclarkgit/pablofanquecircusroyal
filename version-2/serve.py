from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parent
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(ROOT),**kwargs)
 def send_head(self):
  self.remaining=None
  path=Path(self.translate_path(self.path))
  header=self.headers.get('Range','')
  if path.is_file() and header:
   match=re.fullmatch(r'bytes=(\d+)-(\d*)',header)
   if match:
    size=path.stat().st_size; start=int(match[1]);end=min(int(match[2]) if match[2] else size-1,size-1)
    if start> end:
     self.send_response(416);self.send_header('Content-Range',f'bytes */{size}');self.end_headers();return None
    f=path.open('rb');f.seek(start);self.remaining=end-start+1
    self.send_response(206);self.send_header('Content-Type',self.guess_type(str(path)));self.send_header('Accept-Ranges','bytes');self.send_header('Content-Range',f'bytes {start}-{end}/{size}');self.send_header('Content-Length',str(self.remaining));self.end_headers();return f
  return super().send_head()
 def copyfile(self,source,outputfile):
  try:
   if self.remaining is None:return super().copyfile(source,outputfile)
   while self.remaining:
    data=source.read(min(self.remaining,65536))
    if not data:break
    outputfile.write(data);self.remaining-=len(data)
  except (BrokenPipeError,ConnectionResetError):pass
ThreadingHTTPServer(('127.0.0.1',8765),Handler).serve_forever()
