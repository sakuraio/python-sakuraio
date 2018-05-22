from .project import ProjectMixins
from .file import FileMixins
from .module import ModuleMixins
from .service import ServiceMixins


class APIMixins(ProjectMixins, FileMixins, ModuleMixins, ServiceMixins):
    pass
