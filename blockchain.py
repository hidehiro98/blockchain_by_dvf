# coding: UTF-8

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # 新しいブロックを作り、チェーンに加える
        pass

    def new_transaction(self):
        #　新しいトランザクションをリストに加える
        pass

    @staticmethod
    def hash(block):
        # ブロックをハッシュ化する
        pass

    @property
    def last_block(self):
        # チェーンの最後のブロックをリターンする
        pass
