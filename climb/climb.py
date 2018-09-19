"""
ͨ��б�ʵ�ƽ��ֵ��Ѱ�Ҳ���Ͳ��ȣ�����һ���ھֲ����ܴ��ڲ����������������ϳ��ֲ�����ͨ��������ƽ��ֵ
"""
import numpy as np

class VarClimb(object):
    """
    ͨ�����������˲�����ʹ�������㷨��
    ����һ�������������ĵ㶼��ƽ��ֵ��������Ӷ�����ĳ����Ĳ�����ɵĲ���
    """
    def __init__(self, data:list, step: int = 5):
        """

        :param data: һ��һά����
        :param step: ����
        :param r: ��ֵ
        """
        self.data = np.array(data)
        self.step = step

    def get_means_array(self):
        """
        �����ݽ��дֻ�
        :return:
        """
        l = self.data.size//self.step
        self.data = self.data[:l * self.step]
        arr = np.reshape(self.data, (l,self.step))
        for i, a in enumerate(arr):
            self.data[i * self.step:(i + 1) * self.step] = np.array([np.sum(a)/self.step for j in range(self.step)])

        return self.data

    def get_peaks_troughs(self):
        """
        ��ȡ����Ͳ����б�
        :return:
        """
        data = self.get_means_array()
        return Climb(data,self.step).get_peaks_troughs()


class Climb(object):
    """
    ����ȡƽ��ֵ���㲨�岨�ȣ�
    ��ȡn��n+step�ĵ��ƽ��ֵ��n+1��n+step+1�ĵ��ƽ��ֵ���бȽϣ�ת�۵��жϲ���Ͳ��ȣ�����ȥ�����š�
    """

    def __init__(self, data: list, step: int = 5):
        """
        :param data: һ��һά����
        :param step: ����
        """
        self.data = data
        self.step = step
        self.peaks = list()  # �����б�
        self.troughs = list()  # �����б�
        self.S = list()  # ������ǵ�ǰ�����»������£�1���£�2����
        self.array = None

    def _get_array_two(self):
        """
        ��dataת��Ϊ��ά����
        :return:
        """

        return np.array([self.data[i:i+self.step] for i in range(len(self.data)-self.step + 1)])

    def _get_list_S(self):
        """
        ��ȡ�����µ��б�
        :return:
        """
        if self.S:
            return self.S
        np_data = self._get_array_two()
        self.S.extend([1 if np.sum(np_data[i + 1] - np_data[i]) >= 0 else 2 for i in range(np_data.shape[0] - 1)])
        return self.S

    def get_peaks_troughs(self):
        """
        ��ȡ����Ͳ����б�
        :return:
        """
        S = self._get_list_S()
        if not self.array:
            self.array = self._get_array_two()
        for i in range(len(S)-1):
            if S[i + 1] > S[i]:
                self.peaks.append(np.median(self.array[i + 1]))
            elif S[i + 1] < S[i]:
                self.troughs.append(np.median(self.array[i + 1]))
        print(self.data)

        return self.peaks, self.troughs

    def get_number_peaks_troughs(self):
        """
        ��ȡ����Ͳ��ȵ�����
        :return:
        """
        self.get_peaks_troughs()
        return len(self.peaks), len(self.troughs)




if __name__ == '__main__':
    pass
