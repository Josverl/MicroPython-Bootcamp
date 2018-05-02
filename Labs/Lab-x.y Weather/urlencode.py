def urlencode(query, doseq=False, safe='', encoding=None, errors=None):
    """Encode a dict or sequence of two-element tuples into a URL query string.

    If any values in the query arg are sequences and doseq is true, each
    sequence element is converted to a separate parameter.

    If the query arg is a sequence of two-element tuples, the order of the
    parameters in the output will match the order of parameters in the
    input.

    The components of a query arg may each be either a string or a bytes type.
    When a component is a string, the safe, encoding and error parameters are
    sent to the quote_plus function for encoding.
    """

    if hasattr(query, "items"):
        query = query.items()
    else:
        # It's a bother at times that strings and string-like objects are
        # sequences.
        try:
            # non-sequence items should not work with len()
            # non-empty strings will fail this
            if len(query) and not isinstance(query[0], tuple):
                raise TypeError
            # Zero-length sequences of all types will get here and succeed,
            # but that's a minor nit.  Since the original implementation
            # allowed empty dicts that type of behavior probably should be
            # preserved for consistency
        except TypeError:
#            ty, va, tb = sys.exc_info()
            raise TypeError("not a valid non-string sequence "
                            "or mapping object")#.with_traceback(tb)

    l = []
    if not doseq:
        for k, v in query:
            if isinstance(k, bytes):
                k = quote_plus(k, safe)
            else:
                k = quote_plus(str(k), safe, encoding, errors)

            if isinstance(v, bytes):
                v = quote_plus(v, safe)
            else:
                v = quote_plus(str(v), safe, encoding, errors)
            l.append(k + '=' + v)
    else:
        for k, v in query:
            if isinstance(k, bytes):
                k = quote_plus(k, safe)
            else:
                k = quote_plus(str(k), safe, encoding, errors)

            if isinstance(v, bytes):
                v = quote_plus(v, safe)
                l.append(k + '=' + v)
            elif isinstance(v, str):
                v = quote_plus(v, safe, encoding, errors)
                l.append(k + '=' + v)
            else:
                try:
                    # Is this a sufficient test for sequence-ness?
                    x = len(v)
                except TypeError:
                    # not a sequence
                    v = quote_plus(str(v), safe, encoding, errors)
                    l.append(k + '=' + v)
                else:
                    # loop over the sequence
                    for elt in v:
                        if isinstance(elt, bytes):
                            elt = quote_plus(elt, safe)
                        else:
                            elt = quote_plus(str(elt), safe, encoding, errors)
                        l.append(k + '=' + elt)
    return '&'.join(l)

