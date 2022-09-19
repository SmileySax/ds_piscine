import sys
import config
import analytics


def main():
    research = analytics.Research(config.DATA_PATH)
    try:
        res = research.file_reader(has_header=config.HAS_HEADER)
        # print(res)
    except Exception as error:
        print("There is an error:", error)
        return
    analys = analytics.Research.Analytics(res)
    sums = analys.counts()
    # print(*sums)
    percents = analys.fractions(*sums)
    # print(*percents)
    rnds = analys.predict_random(3)
    # print(rnds)
    last = analys.predict_last()
    # print(last)
    rnds_stat = analys.counts_given(rnds)
    report = config.REPORT.format(n_obs = sums[0] + sums[1],
                                  tails = sums[1],
                                  heads = sums[0],
                                  p_tails = percents[1],
                                  p_heads = percents[0],
                                  n_preds = config.N_OF_PREDICTIONS,
                                  pr_tails = rnds_stat[1],
                                  pr_heads = rnds_stat[0])
    analys.save_file(report, 'report', 'txt')
    research.sent_notification(True)


if __name__ == '__main__':
    main()