from log_utils import logger


class BullshitGenerator:

    def __init__(self):
        self.template = 'ab是怎么回事呢？a相信大家都很熟悉，但是ab是怎么回事呢，下面就让小编带大家一起了解吧。\nab，其实就是c，大家可能会很惊讶怎么会c呢？但事实就是这样，小编也感到非常惊讶。\n' \
                        '这就是关于ab的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！ '

    def main(self, a, b, c):
        """
        根据上面模板生成小编体废话
        :param a: 主体
        :param b: 事件
        :param c: 别名
        :return: 完整的小编体废话
        """
        logger.info(f'废话生成器接收的参数:{a} {b} {c}')
        bullshit = self.template.replace('a', a).replace('b', b).replace('c', c)
        return bullshit
