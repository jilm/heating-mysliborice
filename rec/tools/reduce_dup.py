
import sys
import config
import pathlib
import daq

work_path = pathlib.Path(config.WORK_DIR)
arch_path = pathlib.Path(config.ARCH_DIR)
work_files = work_path.glob('*.arch')
for wf in work_files:
    # create coresponding arch file
    name = wf.name
    arch_name = pathlib.Path(arch_path, name)
    with open(arch_name, 'w') as arch_file:
        for t, v in daq.reduce_dup(daq.raw_read_from_file(wf)):
            arch_file.write('{},{}\n'.format(t, v))

