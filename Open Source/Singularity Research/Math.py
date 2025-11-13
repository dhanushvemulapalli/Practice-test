from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
import numpy as np

class WolframMatrix:
    def __init__(self, matrix, session=None):
        """
        matrix : Python list-of-lists or numpy array
        session: optional WolframLanguageSession. If None, create a private session.
        """
        self.A = np.array(matrix, dtype=float).tolist()
        self.session = session or WolframLanguageSession()
        self._own_session = session is None

    def __del__(self):
        if self._own_session:
            try: self.session.terminate()
            except: pass

    # -------------------------------------------------------------
    # internal helper
    # -------------------------------------------------------------
    def _wl(self, func):
        """Evaluate a Wolfram Language expression and return Python result."""
        return self.session.evaluate(func)

    # -------------------------------------------------------------
    # Eigenvalues / Eigenvectors
    # -------------------------------------------------------------
    def eigen(self):
        expr = wl.Eigensystem(self.A)
        vals, vecs = self._wl(expr)
        # Convert to numpy for convenience
        vals = np.array(vals, dtype=float)
        vecs = np.array(vecs, dtype=float).T  # WL returns eigenvectors as rows
        return vals, vecs

    # -------------------------------------------------------------
    # SVD
    # -------------------------------------------------------------
    def svd(self):
        U, S, V = self._wl(wl.SingularValueDecomposition(self.A))
        U = np.array(U, dtype=float)
        svals = np.array([S[i][i] for i in range(min(len(S), len(S[0])))], dtype=float)
        Vt = np.array(V, dtype=float).T
        return U, svals, Vt

    # -------------------------------------------------------------
    # QR factorization
    # -------------------------------------------------------------
    def qr(self):
        Q, R = self._wl(wl.QRDecomposition(self.A))
        return np.array(Q, dtype=float), np.array(R, dtype=float)

    # -------------------------------------------------------------
    # Inverse (or pseudo-inverse)
    # -------------------------------------------------------------
    def inverse(self):
        rows, cols = len(self.A), len(self.A[0])
        if rows == cols:
            det = self._wl(wl.Det(self.A))
            if abs(det) > 1e-12:
                invA = self._wl(wl.Inverse(self.A))
                return np.array(invA, dtype=float)
        # fallback: pseudoinverse
        pinv = self._wl(wl.PseudoInverse(self.A))
        return np.array(pinv, dtype=float)

    # -------------------------------------------------------------
    # Pretty printing
    # -------------------------------------------------------------
    def __repr__(self):
        return f"WolframMatrix({np.array(self.A)})"

from wolframclient.evaluation import WolframLanguageSession

session = WolframLanguageSession()

A = WolframMatrix([[5, 2, 1],
                   [2, 3, 0],
                   [1, 0, 4]], session=session)

vals, vecs = A.eigen()
print(vals)
print(vecs)

U, s, Vt = A.svd()
print(s)

Q, R = A.qr()
print(Q)
print(R)

invA = A.inverse()
print(invA)
