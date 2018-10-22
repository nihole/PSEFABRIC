# https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch04s26.html

def VersionFile(file_spec, vtype='copy'):
    import os, shutil

    if os.path.isfile(file_spec):

        # Determine root filename so the extension doesn't get longer
        n, e = os.path.splitext(file_spec)

        # Is e an integer?
        try:
             num = int(e)
             root = n
        except ValueError:
             root = file_spec

        # Find next available file version
        last_ = 0
        for i in xrange(1000):
            file_ = '%s.%03d' % (root, i)
            if not os.path.isfile(file_):
                last_ = i-1
                break
        for j in xrange(last_, -1, -1):
            old_file = '%s.%03d' % (root, j)
            new_file = '%s.%03d' % (root, j+1)
            shutil.copy(old_file, new_file)
        shutil.copy(root, '%s.%03d' % (root, 0))    
    return 1

if __name__ == '__main__':
      # test code (you will need a file named test.txt)
      print VersionFile('test.txt')
      print VersionFile('test.txt')
