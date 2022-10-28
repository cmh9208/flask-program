from dataclasses import dataclass


@dataclass  # 외부 대량의 데이터를 읽음 ,다른곳에서 가공을하더라고 지워지지 않음(저장되있음)
class Dataset(object):
    context: str  # context 는 경로 str 은 스트링
    fname: str  # 파일명
    train: object  # train.csv 가 데이터 프레임 으로 전환된 객체
    test: object  # test.csv 가 데이터 프레임 으로 전환된 객체
    id: str  # 승객 ID 로 문제가 된다
    label: str  # 승객 ID에 따른 생존 여부로 답이 된다.

    # 데이터를 읽고(getter = 프로퍼티) / 쓰기(setter) 기능을 추가한다.
    # 메모리 전역 공간
    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label
