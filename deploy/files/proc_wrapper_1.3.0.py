#!/usr/local/bin/python3
import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
# Copyright 2020 CloudReactor Inc. All rights reserved.