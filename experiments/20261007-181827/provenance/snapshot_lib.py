import os,hashlib,stat,subprocess,datetime
from pathlib import Path

def now():
 return datetime.datetime.now(datetime.timezone.utc).isoformat()

def git(p,*args):
 env=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
 r=subprocess.run(['git','-c','core.fsmonitor=false','-C',str(p),*args],env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 return {'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}

def manifest(root,exclude_git=True):
 root=Path(root); out={}
 def visit(d):
  for q in sorted(d.iterdir()):
   if exclude_git and q.name=='.git': continue
   rel=q.relative_to(root).as_posix(); st=q.lstat()
   info={'mode':oct(stat.S_IMODE(st.st_mode)),'mtime_ns':st.st_mtime_ns}
   if q.is_symlink(): info.update(kind='symlink',target=os.readlink(q))
   elif q.is_dir():
    info.update(kind='directory');out[rel]=info;visit(q);continue
   elif q.is_file():
    h=hashlib.sha256()
    with q.open('rb') as f:
     for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
    after=q.stat()
    info.update(kind='file',size=st.st_size,sha256=h.hexdigest(),stable_during_read=(st.st_size,st.st_mtime_ns)==(after.st_size,after.st_mtime_ns))
   else:info.update(kind='special',size=st.st_size)
   out[rel]=info
 visit(root);return out

def snapshot(p):
 p=Path(p)
 return {'path':str(p),'captured_at_utc':now(),'working_tree':manifest(p),'git_state':{key:git(p,*args) for key,args in {'status':['status','--porcelain=v2','--branch','--untracked-files=all'],'head':['rev-parse','--verify','HEAD'],'branch':['symbolic-ref','-q','HEAD'],'refs':['show-ref'],'diff':['diff','--binary'],'cached_diff':['diff','--cached','--binary']}.items()},'git_metadata':manifest(p/'.git',False) if (p/'.git').is_dir() else None}
