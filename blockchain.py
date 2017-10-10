# coding: UTF-8

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # 新しいブロックを作り、チェーンに加える
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        次に採掘されるブロックに加える新しいトランザクションを作る
        :param sender: <str> 送信者のアドレス
        :param recipient: <str> 受信者のアドレス
        :param amount: <int> 量
        :return: <int> このトランザクションを含むブロックのアドレス
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # ブロックをハッシュ化する
        pass

    @property
    def last_block(self):
        # チェーンの最後のブロックをリターンする
        pass
