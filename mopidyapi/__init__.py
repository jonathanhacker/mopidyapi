"""
MopidyAPI
~~~~~~~~~
MopidyAPI is a Python (3.6+) library for interacting with Mopidy,
using its JSON RPC API.
"""

__all__ = ['MopidyAPI', 'client', 'wsclient', 'exceptions']
__version__ = '1.0.0'

from .client import MopidyAPI
from .wsclient import MopidyWSClient
