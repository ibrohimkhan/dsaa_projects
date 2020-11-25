from collections import defaultdict


class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = defaultdict(RouteTrieNode)

    def insert(self, path):
        self.children[path] = RouteTrieNode()


class RouteTrie:
    def __init__(self, handler=None):
        self.root = RouteTrieNode(handler)

    def insert(self, route, handler):
        current_node = self.root

        for path in route:
            current_node.insert(path)
            current_node = current_node.children[path]

        current_node.handler = handler

    def find(self, route):
        current_node = self.root

        for path in route:
            if path not in current_node.children:
                return None

            current_node = current_node.children[path]

        return current_node.handler


class Router:
    def __init__(self, handler, error_handler):
        self.routeTrie = RouteTrie(handler)
        self.error_handler = error_handler

    def add_handler(self, route, handler):
        path = self.split_path(route)
        self.routeTrie.insert(path, handler)

    def lookup(self, route):
        path = self.split_path(route)
        handler = self.routeTrie.find(path)

        if handler is None:
            return self.error_handler
        else:
            return handler

    def split_path(self, path):
        path = path.strip("/")
        return path.split("/") if path else []


def test():
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    print(router.lookup("/"))
    # should print 'root handler'

    print(router.lookup("/home"))
    # should print 'not found handler'

    print(router.lookup("/home/about"))
    # should print 'about handler'

    print(router.lookup("/home/about/"))
    # should print 'about handler'

    print(router.lookup("/home/about/me"))
    # should print 'not found handler'

    # Edge cases
    print(router.lookup(""))
    # Should print 'root handler'

    print(router.lookup(" "))
    # should print 'not found handler'


if __name__ == '__main__':
    test()
