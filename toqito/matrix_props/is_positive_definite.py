"""Is matrix a positive definite matrix."""
import numpy as np
from toqito.matrix_props import is_hermitian


def is_positive_definite(mat: np.ndarray, rtol: float = 1e-05, atol: float = 1e-08) -> bool:
    r"""
    Check if matrix is positive definite (PD) [WikPD]_.

    Examples
    ==========

    Consider the following matrix

    .. math::
        A = \begin{pmatrix}
                2 & -1 & 0 \\
                -1 & 2 & -1 \\
                0 & -1 & 2
            \end{pmatrix}

    our function indicates that this is indeed a positive definite matrix.

    >>> from toqito.matrix_props import is_positive_definite
    >>> import numpy as np
    >>> A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    >>> is_positive_definite(A)
    True

    Alternatively, the following example matrix :math:`B` defined as

    .. math::
        B = \begin{pmatrix}
                -1 & -1 \\
                -1 & -1
            \end{pmatrix}

    is not positive definite.

    >>> from toqito.matrix_props import is_positive_definite
    >>> import numpy as np
    >>> B = np.array([[-1, -1], [-1, -1]])
    >>> is_positive_definite(B)
    False

    See Also
    ========
    is_positive_semidefinite

    References
    ==========
    .. [WikPD] Wikipedia: Definiteness of a matrix.
        https://en.wikipedia.org/wiki/Definiteness_of_a_matrix

    :param mat: Matrix to check.
    :param rtol: The relative tolerance parameter (default 1e-05).
    :param atol: The absolute tolerance parameter (default 1e-08).
    :return: Return :code:`True` if matrix is positive definite, and :code:`False` otherwise.
    """
    if np.array_equal(mat, mat.conj().T):
        try:
            # Cholesky decomp requires that the matrix in question is
            # positive-definite. It will throw an error if this is not the case
            # that we catch here.
            np.linalg.cholesky(mat)
            return True
        except np.linalg.LinAlgError:
            return False
    else:
        return False