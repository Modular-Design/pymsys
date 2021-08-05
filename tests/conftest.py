from src.pymsys import ILink


def parent_testing(link):
    for _, child in link.get_childs().items():
        if isinstance(child, ILink):
            assert child.get_parent() is link
            parent_testing(child)
